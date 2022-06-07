import numpy as np
import torch
from tqdm import tqdm
from misc.utils import get_device, save_json
import torch.nn.functional as F

DEVICE = get_device()


class ArtefactModel(torch.nn.Module):
    def __init__(self, vocab_size, fusion=0, hidden_size=768, embd_size=512):
        super().__init__()

        self.fusion = fusion

        if fusion == 0:
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
        elif fusion == 1:
            pass

        self.loss = torch.nn.CrossEntropyLoss()
        self.loss_without_reduce = torch.nn.CrossEntropyLoss(reduction="none")
        self.optimizer = torch.optim.Adam(self.parameters(), lr=10e-6)
        self.to(DEVICE)

    def forward(self, x_embd):
        out = self.model_dense(x_embd)
        return out

    def eval_dev(self, data_dev):
        self.train(False)
        losses_dev = []
        with torch.no_grad():
            for sample_num, sent_embd in tqdm(data_dev):
                # future words to predict
                sample_next = sample_num[1:].to(DEVICE)
                sent_embd = sent_embd.to(DEVICE)

                out = self.forward(sent_embd)
                loss = self.loss_without_reduce(out, sample_next)
                losses_dev += loss.detach().cpu().tolist()

        losses_dev = np.average(losses_dev)
        self.train(True)
        return losses_dev

    def train_loop(self, data_train, data_dev, prefix="", epochs=50):
        logdata = []
        for epoch in range(epochs):
            self.train(True)

            losses_train = []
            for sample_i, (sample_num, sent_embd) in enumerate(tqdm(data_train)):
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
                    losses_dev = self.eval_dev(data_dev)

                    # warning: train_loss is macroaverage, dev_loss is microaverage
                    logdata.append({
                        "epoch": epoch,
                        "train_loss": losses_train,
                        "dev_loss": losses_dev,
                        "dev_pp": 2**losses_dev
                    })

                    save_json(
                        f"computed/art_{prefix}-f{self.fusion}.json",
                        logdata
                    )
                    losses_train = []
