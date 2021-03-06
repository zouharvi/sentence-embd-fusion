import numpy as np
import torch
from tqdm import tqdm
from misc.utils import get_device, save_json
import torch.nn.functional as F

DEVICE = get_device()


class LSTMDynamicDropout(torch.nn.Module):
    def __init__(self, vocab_size, ps, fusion=0, hidden_size=768, embd_size=512):
        super().__init__()

        self.fusion = fusion
        self.ps = ps
        self.model_rnn = torch.nn.LSTM(
            input_size=embd_size, hidden_size=hidden_size,
            bidirectional=False, batch_first=True
        )

        # define embedding layers
        self.model_embd_in = torch.nn.Linear(vocab_size, embd_size)
        self.model_embd_out = torch.nn.Linear(embd_size, vocab_size)
        # tie weights
        # self.model_embd_out.weight[:] = self.model_embd_in.weight.T[:]
        # this doesn't work but we can replace the call in forward with:
        # torch.nn.functional.linear(x, self.model_embd_in.weight.T)
        # which results in worse performance, therefore it may be the case it's incorrect

        if fusion == 0:
            self.model_dense = torch.nn.Linear(
                hidden_size + (768 if fusion == 1 else 0),
                embd_size
            )
        elif fusion == 1:
            self.model_dense = torch.nn.Linear(
                hidden_size + 768,
                embd_size
            )
        elif fusion in {2, 3, 4, 5, 6}:  
            assert hidden_size == 768
            self.model_dense = torch.nn.Linear(
                768,
                embd_size
            )

        self.loss = torch.nn.CrossEntropyLoss()
        self.loss_without_reduce = torch.nn.CrossEntropyLoss(reduction="none")
        self.optimizer = torch.optim.Adam(self.parameters(), lr=10e-6)

        self.to(DEVICE)


    def forward(self, x, x_embd, epoch):
        seq_length = x.shape[1]
        x = self.model_embd_in(x)

        # create 1, 2, 3, .. |x| index vector and make a mask out of it
        last_index = F.one_hot(torch.arange(
            0, x.shape[0]), num_classes=seq_length) == True

        # dropout
        p = self.get_ps(epoch)
        x_embd = x_embd.to(DEVICE)
        x_embd = torch.nn.functional.dropout(x_embd, p)

        # take (1) the output and (2) the last item in each sequence
        if self.fusion == 4:
            x_embd = x_embd.reshape(1, *x_embd.shape).to(DEVICE)
            x_embd_2 = torch.zeros(x_embd.shape, device=DEVICE)
            # additionally fuse as the initial state
            x = self.model_rnn(x, (x_embd, x_embd_2))[0][last_index]
        elif self.fusion == 5:
            x_embd = x_embd.reshape(1, *x_embd.shape).to(DEVICE)
            x_embd_2 = torch.zeros(x_embd.shape, device=DEVICE)
            # additionally fuse as the initial state
            x = self.model_rnn(x, (x_embd_2, x_embd))[0][last_index]
        elif self.fusion == 6:
            x_embd = x_embd.reshape(1, *x_embd.shape).to(DEVICE)
            # additionally fuse as the initial state
            x = self.model_rnn(x, (x_embd, x_embd))[0][last_index]
        else:
            # take (1) the output and (2) the last item in each sequence
            x = self.model_rnn(x)[0][last_index]

        # fuse
        if self.fusion == 1:
            x_embd = x_embd.to(DEVICE)
            # x_embd = x_embd.reshape((x.shape[0], -1))
            x = torch.hstack((x, x_embd))
        elif self.fusion == 2:
            x_embd = x_embd.to(DEVICE)
            x = x + x_embd
        elif self.fusion == 3:
            x_embd = x_embd.to(DEVICE)
            x = x * x_embd

        # projection layer
        x = self.model_dense(x)
        x = self.model_embd_out(x)
        return x

    def mask_sample(self, sample):
        seq_length = len(sample)
        # duplicate sample sequence
        # TODO: check the reshaping is correct
        sample = sample.tile(
            (seq_length - 1, 1)
        ).reshape(seq_length - 1, seq_length, -1)

        index_a = torch.arange(
            0, seq_length - 1
        ).reshape(-1, 1).tile((seq_length,))
        index_b = torch.arange(
            0, seq_length
        ).reshape(-1, 1).tile((seq_length - 1,)).T
        # zero future indicies
        sample[index_b > index_a, :] = 0

        return sample

    def eval_dev(self, data_dev, encode_text, epoch):
        self.train(False)
        losses_dev = []
        with torch.no_grad():
            for sample_num, sent_embd in tqdm(data_dev):
                sample = encode_text(sample_num.to(DEVICE))
                sample = self.mask_sample(sample)

                # future words to predict
                sample_next = sample_num[1:].to(DEVICE)

                out = self.forward(sample, sent_embd, epoch)
                loss = self.loss_without_reduce(out, sample_next)
                losses_dev += loss.detach().cpu().tolist()

        losses_dev = np.average(losses_dev)
        self.train(True)
        return losses_dev

    def get_ps(self, epoch,):
        if epoch >= len(self.ps):
            return self.ps[-1]
        else:
            return self.ps[epoch]

    def train_loop(self, data_train, data_dev, encode_text, prefix="", epochs=50):
        logdata = []
        for epoch in range(epochs):
            self.train(True)
            print("Using", self.get_ps(epoch), "with", self.training)

            losses_train = []
            for sample_i, (sample_num, sent_embd) in enumerate(tqdm(data_train)):
                sample = encode_text(sample_num.to(DEVICE))
                sample = self.mask_sample(sample)

                # this yields the next word predictions
                sample_next = sample_num[1:].to(DEVICE)

                out = self.forward(sample, sent_embd, epoch)
                loss = self.loss(out, sample_next)

                # backpropagation
                self.optimizer.zero_grad()
                loss.backward()
                self.optimizer.step()

                losses_train.append(loss.detach().cpu().item())

                # one log step
                if sample_i % 33000 == 0:
                    losses_train = np.average(losses_train)
                    losses_dev = self.eval_dev(data_dev, encode_text, epoch)

                    # warning: train_loss is macroaverage, dev_loss is microaverage
                    logdata.append({
                        "epoch": epoch,
                        "train_loss": losses_train,
                        "dev_loss": losses_dev,
                        "dev_pp": 2**losses_dev
                    })

                    save_json(
                        f"computed/{prefix}-f{self.fusion}.json",
                        logdata
                    )
                    losses_train = []
