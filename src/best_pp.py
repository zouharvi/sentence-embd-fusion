#!/usr/bin/env python3

from misc.utils import read_json
from argparse import ArgumentParser

args = ArgumentParser()
args.add_argument("logfile", nargs="+")
args.add_argument("--corr", action="store_true")
args = args.parse_args()


for f in args.logfile:
    print(f)
    data = read_json(f)

    best_i = None
    if args.corr:
        best_v = float('-inf')
    else:
        best_v = float('inf')

    for line_i, line in enumerate(data):
        if args.corr:
            if line["rt_corr"] > best_v:
                best_i = line_i
                best_v = line["rt_corr"]
        else:
            if line["dev_pp"] < best_v:
                best_i = line_i
                best_v = line["dev_pp"]

    print("!" if best_i+1 == len(data) else " ", f"{best_i+1}/{len(data)}", data[best_i], "\n")