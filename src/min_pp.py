#!/usr/bin/env python3

from misc.utils import read_json
from argparse import ArgumentParser

args = ArgumentParser()
args.add_argument("logfile")
args = args.parse_args()

data = read_json(args.logfile)

min_i = None
min_v = float('inf')

for line_i, line in enumerate(data):
    if line["dev_pp"] < min_v:
        min_i = line_i
        min_v = line["dev_pp"]

print(data[min_i])