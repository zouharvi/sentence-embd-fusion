#!/usr/bin/env python3

from argparse import ArgumentParser
from misc.utils import read_pickle
import torch
import torch.nn.functional as F
import numpy as np
from model_artefact import ArtefactModel

torch.set_num_threads(10)

if __name__ == "__main__":
    args = ArgumentParser()
    args.add_argument("-d", "--data", default="/data/sef/missing.embd")
    args.add_argument("-d2", "--data-dev", default=None)
    args.add_argument("-m", "--model", type=int, default=0)
    args.add_argument("-nn", "--nick-name", default="tmp")
    args.add_argument("-mn", "--model-name", default="bert")
    args.add_argument("-v", "--vocab-size", type=int, default=8192)
    args.add_argument("-e", "--epochs", type=int, default=100)
    args.add_argument("-tn", "--train-n", type=int, default=100000)
    args.add_argument("--encoder", default=None)
    args.add_argument("--prob-file", default=None)
    args.add_argument("--hidden-size", type=int, default=768)
    args = args.parse_args()

    if args.data_dev is not None:
        data_train = read_pickle(args.data)
        data_train = data_train[:args.train_n]
        data_dev = read_pickle(args.data_dev)
        data_dev = data_dev
    else:
        data = read_pickle(args.data)
        data_train = data[:args.train_n]
        data_dev = data[-10000:]

    print(f"Using {len(data_train)} for training")
    print(f"Using {len(data_dev)} for dev")

    data_dev = [
        (x[0], torch.LongTensor(np.array(x[1])), torch.FloatTensor(np.array(x[2])))
        for x in data_dev
    ]

    data_train = [
        (x[0], torch.LongTensor(np.array(x[1])), torch.FloatTensor(np.array(x[2])))
        for x in data_train
    ]

    if args.encoder is not None:
        encoder = read_pickle(args.encoder)
    else:
        encoder = None

    model = ArtefactModel(
        args.vocab_size, model_arch=args.model,
        encoder=encoder,
    )
    model.train_loop(
        data_train, data_dev,
        prefix=f"art_{args.model_name}-{args.nick_name}",
        epochs=args.epochs,
        prob_file=args.prob_file,
    )
