import numpy as np
import torch
from tqdm import tqdm
from misc.utils import get_device, save_json
import torch.nn.functional as F

DEVICE = get_device()

class LSTMModel(torch.nn.Module):
    def __init__(self, vocab_size, fusion=0, hidden_size=256):
        super().__init__()

        self.fusion = fusion
        self.model_rnn = torch.nn.LSTM(input_size=vocab_size, hidden_size=hidden_size, bidirectional=True, batch_first=True)
        self.model_dense = torch.nn.Linear(
            2*hidden_size+(768 if fusion == 1 else 0),
            vocab_size
        )

        self.loss = torch.nn.CrossEntropyLoss()
        self.loss_without_reduce = torch.nn.CrossEntropyLoss(reduction="none")
        self.optimizer = torch.optim.Adam(self.parameters(), lr=10e-3)

        self.to(DEVICE)

    def forward(self, x, x_embd):
        seq_length = x.shape[1]

        # create 1, 2, 3, .. |x| index vector and make a mask out of it
        last_index = F.one_hot(torch.arange(0, x.shape[0]), num_classes=seq_length) == True
        # take the (1) all sequence in the batch, (2) the output and (3) the last item in each sequence
        x = self.model_rnn(x)[0][last_index]

        # fuse
        if self.fusion == 1:
            x_embd = torch.FloatTensor(x_embd).to(DEVICE)
            x_embd = x_embd.tile((x.shape[0],)).reshape((x.shape[0], -1))
            x = torch.hstack((x, x_embd))

        # projection layer
        x = self.model_dense(x)

        return x
    
    def mask_sample(self, sample):
        seq_length = len(sample)
        sample = sample.to(DEVICE)
        # duplicate sample sequence
        # TODO: check the resamping is correct
        sample = sample.tile((seq_length-1,1)).reshape(seq_length-1, seq_length, -1)

        index_a = torch.arange(0, seq_length-1).reshape(-1, 1).tile((seq_length,))
        index_b = torch.arange(0, seq_length).reshape(-1, 1).tile((seq_length-1,)).T
        # zero future indicies
        sample[index_b>index_a,:] = 0

        return sample

    def train_loop(self, data_train, data_dev, prefix="", epochs=10):
        logdata = []
        for epoch in range(epochs):
            self.train(True)

            losses_train = []
            for sample, sample_num, sent_embd in tqdm(data_train):
                sample = self.mask_sample(sample)

                # trick to keep this a tensor with (1, 1) shape 
                sample_next = sample_num[1:].to(DEVICE)

                out = self.forward(sample, sent_embd)
                loss = self.loss(out, sample_next)
                
                # backpropagation
                self.optimizer.zero_grad()
                loss.backward()
                self.optimizer.step()

                losses_train.append(loss.detach().cpu().item())
                
                # free up memory
                del sample_next

            losses_train = np.average(losses_train)
            print(f"Avg. loss: {losses_train:.2f}")

            self.train(False)
            losses_dev = []
            with torch.no_grad():
                for sample, sample_num, sent_embd in tqdm(data_dev):
                    sample = self.mask_sample(sample)

                    # trick to keep this a tensor with (1, 1) shape 
                    sample_next = sample_num[1:].to(DEVICE)
                    
                    out = self.forward(sample, sent_embd)

                    loss = self.loss_without_reduce(out, sample_next)

                    losses_dev += loss.detach().cpu().tolist()

            losses_dev = np.average(losses_dev)
            print(f"Dev pp: {2**losses_dev:.2f}")

            # warning: train_loss is macroaverage, dev_loss is microaverage
            logdata.append({"train_loss": losses_train, "dev_loss": losses_dev, "dev_pp": 2**losses_dev})

            save_json(f"computed/{prefix}-f{self.fusion}.json", logdata)