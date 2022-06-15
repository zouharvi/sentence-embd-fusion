#!/usr/bin/env python3

import sys

import numpy as np
sys.path.append("src")
from misc.utils import read_json
from argparse import ArgumentParser
import fig_utils
import matplotlib.pyplot as plt

args = ArgumentParser()
args.add_argument("--subl", nargs="+")
args.add_argument("--sub-k", type=float, nargs="+")
args.add_argument("--subr", nargs="+")
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

pp_f0 = data_subl[-1]
pp_f1 = data_subl[0]

_fig, ax = plt.subplots(1, 2, figsize=(9, 4), gridspec_kw={'width_ratios': [2.5, 1]})
ax1 = ax[0]
ax2 = ax[1]
ax2.yaxis.set_label_position("right")
ax2.yaxis.tick_right()

# plot first so that they're behind more complex lines
# this should be the same as subl with k=0 or subr with k=1
ax1.hlines(
    y=pp_f0,
    xmin=min(args.sub_k),
    xmax=max(args.sub_k),
    linestyles="--",
    label="Perplexity no fusion",
    color="dimgray",
)
ax1.hlines(
    y=pp_f1,
    xmin=min(args.sub_k),
    xmax=max(args.sub_k),
    linestyles="-.",
    # add fake $$ to normalize line height
    label="Perplexity full prefix $\,$",
    color="dimgray",
)

ax1.plot(
    args.sub_k,
    data_subl,
    label="Perplexity left crop ($\min(i, k\cdot |S|) \\rightarrow i$)",
    color="cornflowerblue",
    marker="o", ms=7,
)
ax1.plot(
    args.sub_k,
    data_subr,
    label="Perplexity right crop ($0 \\rightarrow \min(i, k\cdot |S|)$)",
    color="salmon",
    marker="^", ms=7,
)
ax1.set_ylabel("Dev Perplexity")
ax2.set_ylabel("Similarity to whole prefix")
ax1.set_xlabel("$k$")
ax2.set_xlabel("$k$")


# plot similarities
ax2.plot(
    SIM_KEYS,
    [SIM_SUBL[k] for k in SIM_KEYS],
    # add fake $$ to normalize line height
    label="Similarity left crop $\,$",
    linestyle=":",
    marker="o", ms=7,
)
ax2.plot(
    SIM_KEYS,
    [SIM_SUBR[k] for k in SIM_KEYS],
    # add fake $$ to normalize line height
    label="Similarity right crop $\,$",
    linestyle=":",
    marker="^", ms=7,
)

ax2.set_yticks(list(np.linspace(0.88, 1.0, 5)))
ax1.set_xticks(args.sub_k, [f"{x:.0%}" for x in args.sub_k])
ax2.set_xticks(args.sub_k[1:-1], [f"{x:.0%}" for x in args.sub_k[1:-1]])

h1, l1 = ax1.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
LEGEND_PERM = [2, 3, 0, 4, 5, 1]

plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.01, hspace=None)

ax1.legend(
    h1, l1,
    loc="upper left",
    bbox_to_anchor=(-0.011, 1.26),
    ncol=2,
)
ax2.legend(
    h2, l2,
    loc="upper left",
    bbox_to_anchor=(0.016, 1.26),
    ncol=1,
)
plt.tight_layout(rect=(0, 0, 1, 1.01), pad=0)
plt.savefig("figures/sub_feeders.pdf")
plt.show()
