#!/usr/bin/env python3

from misc.utils import read_pickle
from argparse import ArgumentParser

args = ArgumentParser()
args.add_argument(
    "-l", "--logfile",
    default="computed/moctezuma_full_probs.pkl"
)
args.add_argument("-i", type=int, default=64)
args = args.parse_args()

data = read_pickle(args.logfile)
vocab = data["vocab"]
print("total", len(data["probs"]))
print("epoch", data["probs"][args.i]["epoch"])


def extract_tokens(sent_i):
    probs = data["probs"][args.i]["probs"][sent_i]["probs"]
    # take the beginning of "conquistadors"
    probs = probs[-3]
    line = [(v, p) for v, p in zip(vocab, probs) if len(v) >= 5]
    line = sorted(line, reverse=False, key=lambda x: x[1])[-40:]
    return set([v for v, p in line])


words_a = extract_tokens(0)
words_b = extract_tokens(1)

print("A ONLY:", data["probs"][args.i]["probs"][0]["txt"])
print(" ".join([f"{v:>15}" for v in words_a - words_b]))
print("B ONLY:", data["probs"][args.i]["probs"][1]["txt"])
print(" ".join([f"{v:>15}" for v in words_b - words_a]))
