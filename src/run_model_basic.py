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
    args.add_argument("-d", "--data", default="/data/sef/missing.embd")
    args.add_argument("-d2", "--data-dev", default=None)
    args.add_argument("-f", "--fusion", type=int, default=0)
    args.add_argument("-nn", "--nick-name", default="")
    args.add_argument("-mn", "--model-name", default="bert")
    args.add_argument("-v", "--vocab-size", type=int, default=8192)
    args.add_argument("-e", "--epochs", type=int, default=100)
    args.add_argument("-tn", "--train-n", type=int, default=100000)
    args.add_argument("--hidden-size", type=int, default=768)
    args = args.parse_args()

    # crop text
    # text = ["BOS " + x[0] + " EOS" for x in data]

    def encode_text(text):
        return (F.one_hot(text, num_classes=args.vocab_size)).float()

    if args.data_dev is not None:
        data_train = read_pickle(args.data)
        data_train = data_train[:args.train_n]
        data_dev = read_pickle(args.data_dev)
        data_dev = data_dev
    else:
        data = read_pickle(args.data)
        data_train = data[:args.train_n]
        data_dev = data[-10000:]

    print(f"Loaded {len(data)}")
    print(f"Using {len(data_train)} for training")
    print(f"Using {len(data_dev)} for dev")

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
        prefix=f"{args.model_name}-{args.nick_name}",
        epochs=args.epochs
    )
