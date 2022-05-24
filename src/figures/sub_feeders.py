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

SIM_SUBR = {0.25: 0.9710434, 0.5: 0.9886881, 0.75: 0.99640083}
SIM_SUBL = {0.25: 0.9392243, 0.5: 0.9037414, 0.75: 0.8756343}
SIM_KEYS = [0.25, 0.5, 0.75]

data_subl = []
for f in args.subl:
    data_subl.append(min([x["dev_pp"] for x in read_json(f)]))
data_subr = []
for f in args.subr:
    data_subr.append(min([x["dev_pp"] for x in read_json(f)]))

fig = plt.figure(figsize=(6, 4))
ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.plot(
    args.subl_k,
    data_subl,
    label="Left crop ($\min(i, k\cdot |S|) \\rightarrow i$)",
    color="cornflowerblue",
)
ax1.plot(
    args.subr_k,
    data_subr,
    label="Right crop ($0 \\rightarrow \min(i, k\cdot |S|)$)",
    color="salmon",
)
ax1.set_ylabel("Dev Perplexity")
ax2.set_ylabel("Similarity to Whole Prefix")
ax1.set_xlabel("$k$")

if args.pp_f0 is not None:
    ax1.hlines(
        y=args.pp_f0,
        xmin=min(args.subl_k+ args.subr_k),
        xmax=max(args.subl_k+ args.subr_k),
        linestyles="-.",
        label="No fusion",
        color="dimgray",
    )
# this should be the same as subl with k=0 or subr with k=1
if args.pp_f1 is not None:
    ax1.hlines(
        y=args.pp_f1,
        xmin=min(args.subl_k+ args.subr_k),
        xmax=max(args.subl_k+ args.subr_k),
        linestyles="-.",
        label="Full prefix",
        color="seagreen",
    )

# plot similarities
ax2.plot(
    SIM_KEYS,
    [SIM_SUBL[k] for k in SIM_KEYS],
    label="Similarity left crop",
    linestyle=":",
    marker=".", ms=10,
)
ax2.plot(
    SIM_KEYS,
    [SIM_SUBR[k] for k in SIM_KEYS],
    label="Similarity right crop",
    linestyle=":",
    marker=".", ms=10,
)

h1, l1 = ax1.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
LEGEND_PERM = [0, 1, 2, 4, 5, 3]

plt.tight_layout(rect=(0, 0, 1, 0.78), pad=0.1)
plt.legend(
    [(h1+h2)[i] for i in LEGEND_PERM],
    [(l1+l2)[i] for i in LEGEND_PERM],
    loc="upper left",
    bbox_to_anchor=(0.0, 1.36),
    ncol=2,
)
plt.savefig("computed/sub_feeders.pdf")
plt.show()
