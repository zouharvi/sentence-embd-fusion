import numpy as np
import torch
from tqdm import tqdm
from misc.utils import get_device, save_pickle, save_json
import torch.nn.functional as F

DEVICE = get_device()


class ArtefactModel(torch.nn.Module):
    def __init__(self, vocab_size, model_arch=0, encoder=None):
        super().__init__()

        self.fusion = model_arch

        if model_arch == 0:
            self.model_dense = torch.nn.Sequential(
                torch.nn.Linear(
                    768, 768,
                ),
                torch.nn.ReLU(),
                torch.nn.Linear(
                    768, 768,
                ),
                torch.nn.ReLU(),
                torch.nn.Linear(
                    768, vocab_size,
                ),
            )
        elif model_arch == 1:
            pass

        if encoder is not None:
            self.encoder = encoder
            vocab = [
                list(encoder.inverse_transform([[i]]))[0]
                for i in range(vocab_size)
            ]
            self.prob_log = {"vocab": vocab, "probs": []}

        self.loss = torch.nn.CrossEntropyLoss()
        self.loss_without_reduce = torch.nn.CrossEntropyLoss(reduction="none")
        self.optimizer = torch.optim.Adam(self.parameters(), lr=10e-6)
        self.to(DEVICE)

    def forward(self, x_embd):
        out = self.model_dense(x_embd)
        return out

    def eval_dev(self, data_dev, epoch, prob_file=None):
        self.train(False)
        losses_dev = []
        with torch.no_grad():
            prob_log_epoch = []
            for sent_txt, sample_num, sent_embd in tqdm(data_dev):
                # future words to predict
                sample_next = sample_num[1:].to(DEVICE)
                sent_embd = sent_embd.to(DEVICE)

                out = self.forward(sent_embd)

                # special info for an experiment
                if prob_file is not None:
                    sent_probs = []
                    for out_w in out:
                        named_out = [float(x) for x in out_w]
                        sent_probs.append(named_out)
                    prob_log_epoch.append({
                        "txt": sent_txt, "probs": sent_probs
                    })

                loss = self.loss_without_reduce(out, sample_next)
                losses_dev += loss.detach().cpu().tolist()

            self.prob_log["probs"].append({"epoch": epoch, "probs": prob_log_epoch})
            save_pickle(prob_file, self.prob_log)
        losses_dev = np.average(losses_dev)
        self.train(True)
        return losses_dev

    def train_loop(self, data_train, data_dev, prefix="", epochs=50, prob_file=None):
        logdata = []
        for epoch in range(epochs):
            self.train(True)

            losses_train = []
            for sample_i, (sent_txt, sample_num, sent_embd) in enumerate(tqdm(data_train)):
                # this yields the next word predictions
                sample_next = sample_num[1:].to(DEVICE)
                sent_embd = sent_embd.to(DEVICE)

                out = self.forward(sent_embd)
                loss = self.loss(out, sample_next)

                # backpropagation
                self.optimizer.zero_grad()
                loss.backward()
                self.optimizer.step()

                losses_train.append(loss.detach().cpu().item())

                # one log step
                if sample_i % 33000 == 0:
                    losses_train = np.average(losses_train)
                    losses_dev = self.eval_dev(
                        data_dev, epoch, prob_file=prob_file)

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
