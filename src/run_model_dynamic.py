#!/usr/bin/env python3

from bpe import Encoder
from argparse import ArgumentParser
from misc.utils import read_pickle
import torch
import torch.nn.functional as F
import numpy as np
from model_dynamic_dropout import LSTMDynamicDropout

if __name__ == "__main__":
    args = ArgumentParser()
    args.add_argument("-d", "--data", default="computed/bert-10000.embd")
    args.add_argument("-f", "--fusion", type=int, default=0)
    args.add_argument("-nn", "--nick-name", default="")
    args.add_argument("-mn", "--model-name", default="bert")
    args.add_argument("-v", "--vocab-size", type=int, default=1024)
    args.add_argument("--hidden-size", type=int, default=768)
    args.add_argument("-e", "--epochs", type=int, default=100)
    args.add_argument("--ps")
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

    if args.ps == "0to1":
        ps = [0.0] * 15 + [0.25] * 15 + [0.5] * 15 + [0.75] * 15 + [1.0] * 15
    elif args.ps == "1to0":
        ps = [1.0] * 15 + [0.75] * 15 + [0.5] * 15 + [0.25] * 15 + [0.0] * 15
    else:
        raise Exception("Unknown ps dropout configuration")

    model = LSTMDynamicDropout(args.vocab_size, fusion=args.fusion, hidden_size=args.hidden_size, ps=ps)

    model.train_loop(
        data[:-1000], data[-1000:],
        encode_text,
        prefix=f"{args.model_name}-{args.nick_name}",
        epochs=args.epochs,
    )
