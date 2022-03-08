#!/usr/bin/env python3

from bpe import Encoder
from argparse import ArgumentParser
from misc.utils import read_pickle
import torch
import torch.nn.functional as F

from model import LSTMModel

if __name__ == "__main__":
    args = ArgumentParser()
    args.add_argument("-d", "--data", default="computed/bert-10000.embd")
    args.add_argument("-t", "--train-data", type=int, default=5000)
    args.add_argument("-v", "--vocab-size", type=int, default=1024)
    args.add_argument("-f", "--fusion", type=int, default=0)
    args = args.parse_args()

    encoder = Encoder(vocab_size=args.vocab_size)
    
    data = read_pickle(args.data)
    text = ["BOS " + x[0] + " EOS" for x in data]

    encoder.fit(text)

    data = zip(
        [torch.LongTensor(x) for x in encoder.transform(text)],
        [x[1] for x in data]
    )

    data =[
        (
            (F.one_hot(x[0], num_classes=args.vocab_size)).float(),
            x[0],
            x[1],
        )
        for x in data
    ]
    
    model = LSTMModel(args.vocab_size, fusion=args.fusion)
    model.train_loop(data[:args.train_data], data[-1000:], prefix="bert-10000", epochs=10)
    # print(next(data))
    # print(data[0][0].shape)
    # print(len(data[0][0]))
    # print([sum(x) for x in data[0][0]])