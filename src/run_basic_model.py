#!/usr/bin/env python3

from bpe import Encoder
from argparse import ArgumentParser
from misc.utils import read_pickle
import torch
import torch.nn.functional as F
import numpy as np
from model_basic import LSTMModel

if __name__ == "__main__":
    args = ArgumentParser()
    args.add_argument("-d", "--data", default="/data/sef/bert-5000-p.embd")
    args.add_argument("-d2", "--data-dev", default=None)
    args.add_argument("-f", "--fusion", type=int, default=0)
    args.add_argument("-p", "--prefix", default="")
    args.add_argument("-mp", "--model-prefix", default="bert")
    args.add_argument("-v", "--vocab-size", type=int, default=1024)
    args.add_argument("-e", "--epochs", type=int, default=50)
    args.add_argument("--hidden-size", type=int, default=768)
    args = args.parse_args()

    # crop text
    # text = ["BOS " + x[0] + " EOS" for x in data]

    def encode_text(text):
        return (F.one_hot(text, num_classes=args.vocab_size)).float()

    if args.data_dev is not None:
        data_train = read_pickle(args.data)
        data_train = data_train[:-1000]
        data_dev = read_pickle(args.data_dev)
        data_dev = data_dev[-1000:]
    else:
        data = read_pickle(args.data)
        data_train = data[:-1000]
        data_dev = data[-1000:]

    data_dev = [
        (torch.LongTensor(np.array(x[1])), torch.FloatTensor(np.array(x[2])))
        for x in data_dev
    ]

    data_train = [
        (torch.LongTensor(np.array(x[1])), torch.FloatTensor(np.array(x[2])))
        for x in data_train
    ]

    model = LSTMModel(args.vocab_size, fusion=args.fusion, hidden_size=args.hidden_size)
    model.train_loop(
        data_train, data_dev,
        encode_text,
        prefix=f"{args.model_prefix}-{args.prefix}",
        epochs=args.epochs
    )
