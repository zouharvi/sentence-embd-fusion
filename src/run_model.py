#!/usr/bin/env python3

from bpe import Encoder
from argparse import ArgumentParser
from misc.utils import read_pickle
import torch
import torch.nn.functional as F
import numpy as np
from model import LSTMModel

if __name__ == "__main__":
    args = ArgumentParser()
    args.add_argument("-d", "--data", default="computed/bert-10000.embd")
    args.add_argument("-f", "--fusion", type=int, default=0)
    args.add_argument("-p", "--prefix", default="")
    args.add_argument("-v", "--vocab-size", type=int, default=1024)
    args.add_argument("-e", "--epochs", type=int, default=10)
    args = args.parse_args()

    data = read_pickle(args.data)
    # crop text
    # text = ["BOS " + x[0] + " EOS" for x in data]

    def encode_text(text):
        return (F.one_hot(text, num_classes=args.vocab_size)).float()

    data = [
        (torch.LongTensor(np.array(x[1])), torch.FloatTensor(np.array(x[2])))
        for x in data
    ]

    model = LSTMModel(args.vocab_size, fusion=args.fusion)
    model.train_loop(
        data[:-1000], data[-1000:],
        encode_text,
        prefix=f"bert-{args.prefix}",
        epochs=args.epochs
    )
