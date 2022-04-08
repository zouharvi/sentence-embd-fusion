#!/usr/bin/env python3

from argparse import ArgumentParser
from utils import read_pickle, save_pickle
import numpy as np
from tqdm import tqdm
import random

shuffled = lambda l: sorted(l, key=lambda k: random.random())

if __name__ == "__main__":
    args = ArgumentParser()
    args.add_argument("-d1", "--data-in", default="/data/sef/bert-5000-p.embd")
    args.add_argument("-d2", "--data-out", default="/data/sef/bert-5000-p-shuff1.embd")
    args.add_argument("-s", "--shuffle-mode", type=int, default=1)
    args = args.parse_args()

    data = read_pickle(args.data_in)

    # decolate

    if args.shuffle_mode == 1:
        # shuffle within sentence
        data = [
            (x[0], x[1], shuffled(x[2]))
            for x in tqdm(data)
        ]
        save_pickle(args.data_out, data)

    elif args.shuffle_mode == 2:
        pool_all = shuffled([embd for sent in data for embd in sent[2]])
        # shuffle within sentence
        data = [
            (
                x[0],
                x[1],
                # gradually eat the shuffled pool
                [pool_all.pop(0) for _ in range(len(x[2]))]
            )
            for x in tqdm(data)
        ]

        save_pickle(args.data_out, data)
    else:
        print("No operation")