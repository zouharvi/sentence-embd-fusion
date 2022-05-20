#!/usr/bin/env python3

import matplotlib.pyplot as plt
import sys
sys.path.append("src")
from misc.utils import read_json
from argparse import ArgumentParser
import fig_utils

args = ArgumentParser()
args.add_argument("--subl", nargs="+")
args.add_argument("--subl-k", type=float, nargs="+")
args.add_argument("--subr", nargs="+")
args.add_argument("--subr-k", type=float, nargs="+")
args.add_argument("--pp-f0", type=float)
args.add_argument("--pp-f1", type=float)
args = args.parse_args()

data_subl = []
for f in args.subl:
    data_subl.append(min([x["dev_pp"] for x in read_json(f)]))
data_subr = []
for f in args.subr:
    data_subr.append(min([x["dev_pp"] for x in read_json(f)]))

fig = plt.figure(figsize=(6, 4))

plt.plot(
    args.subl_k,
    data_subl,
    label="Left crop ($k\cdot |S|: \\rightarrow$)",
    color="cornflowerblue",
)
plt.plot(
    args.subr_k,
    data_subr,
    label="Right crop ($\\rightarrow :\min(i, k\cdot |S|)$)",
    color="salmon",
)
plt.ylabel("Dev Perplexity")
plt.xlabel("$k$")

if args.pp_f0 is not None:
    plt.hlines(
        y=args.pp_f0,
        xmin=min(args.subl_k+ args.subr_k),
        xmax=max(args.subl_k+ args.subr_k),
        linestyles="-.",
        label="No fusion",
        color="dimgray",
    )
# this should be the same as subl with k=0 or subr with k=1
if args.pp_f1 is not None:
    plt.hlines(
        y=args.pp_f1,
        xmin=min(args.subl_k+ args.subr_k),
        xmax=max(args.subl_k+ args.subr_k),
        linestyles="-.",
        label="Full prefix",
        color="seagreen",
    )

plt.legend(
    loc="upper left",
    bbox_to_anchor=(0.1, 1.3),
    ncol=2,
)
plt.tight_layout(rect=(0, 0, 1, 1.02), pad=0.3)
plt.show()
