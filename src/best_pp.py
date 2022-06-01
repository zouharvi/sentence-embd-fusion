#!/usr/bin/env python3

from misc.utils import read_json
from argparse import ArgumentParser

args = ArgumentParser()
args.add_argument("logfile", nargs="+")
args = args.parse_args()


for f in args.logfile:
    print(f)
    data = read_json(f)

    min_i = None
    min_v = float('inf')

    for line_i, line in enumerate(data):
        if line["dev_pp"] < min_v:
            min_i = line_i
            min_v = line["dev_pp"]

    print(f"{min_i}/{len(data)}", data[min_i])