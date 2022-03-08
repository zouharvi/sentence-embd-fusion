import numpy as np
import torch
from tqdm import tqdm
from misc.utils import get_device

DEVICE = get_device()

class LSTMModel(torch.nn.Module):
    def __init__(self, vocab_size, hidden_size=256):
        super().__init__()

        self.model_rnn = torch.nn.LSTM(input_size=vocab_size, hidden_size=hidden_size, bidirectional=True, batch_first=True)
        self.model_dense = torch.nn.Linear(2*hidden_size, vocab_size)

        self.loss = torch.nn.CrossEntropyLoss()
        self.optimizer = torch.optim.Adam(self.parameters(), lr=10e-3)

        self.to(DEVICE)

    def forward(self, x):
        # take the (1) first sequence in the batch, (2) the output and (3) the last item
        x = self.model_rnn(x)[0][0][-1]
        # print(x)
        x = self.model_dense(x)
        return x
    
    def train_loop(self, data_train, data_dev, epochs=10):

        for epoch in range(epochs):
            losses = []
            for sample, sample_num, sent_embd in tqdm(data_train[:100]):
                loss = 0

                # left to right, process one sequence
                for i in range(1, len(sample)-1):
                    sample_sub = sample[0:i].reshape(1, i, -1).to(DEVICE)
                    # trick to keep this a tensor with (1, 1) shape 
                    sample_next = sample_num[i:i+1].to(DEVICE)
                    # force batch first shape
                    out = self.forward(sample_sub).reshape(1, -1)
                    loss += self.loss(out, sample_next)
                
                losses.append(loss.cpu().item())
                # backpropagation
                self.optimizer.zero_grad()
                loss.backward()
                self.optimizer.step()

            print(f"Avg. loss: {np.average(losses):.2f}")