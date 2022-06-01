#!/usr/bin/env python3

import sys
sys.path.append("src/")
from misc.utils import read_pickle
from argparse import ArgumentParser

args = ArgumentParser()
args.add_argument("-d", "--data", nargs="+")
args.add_argument("-e", "--encoder", default=None)
args = args.parse_args()

if args.encoder is not None:
    encoder = read_pickle(args.encoder)
else:
    encoder = None

for f in args.data:
    print("Reading", f)
    data = read_pickle(f)
    print(len(data), "sents")
    print(data[0][0])
    print(len(data[0][1]), data[0][1])
    if encoder is not None:
        print(list(encoder.inverse_transform([data[0][1]])))
    print(len(data[0][2]), len(data[0][2][0]), data[0][2][0][:4])

    print()
