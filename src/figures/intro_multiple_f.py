#!/usr/bin/env python3

import sys
sys.path.append("src")
from argparse import ArgumentParser
from misc.utils import read_json
import matplotlib.pyplot as plt
from collections import defaultdict
import numpy as np
import fig_utils

def aggregate_epochs(data):
    # average values across epochs

    data_dict = defaultdict(list)
    for line in data:
        data_dict[line["epoch"]].append(line)

    data_dict = {
        k: {
            "train_loss": np.average([x["train_loss"] for x in v]),
            "dev_pp": np.average([x["dev_pp"] for x in v]),
            "epoch": k
        }
        for k, v in data_dict.items()
    }
    lowest_epoch = min(data_dict.keys())
    data_new = [None for _ in data_dict.keys()]
    for k, v in data_dict.items():
        data_new[k-lowest_epoch] = v
    return data_new

args = ArgumentParser()
args.add_argument("-f0"); args.add_argument("-l0", default="f0")
args.add_argument("-f1"); args.add_argument("-l1", default="f1")
args.add_argument("-f2"); args.add_argument("-l2", default="f2")
args.add_argument("-f3"); args.add_argument("-l3", default="f3")
args.add_argument("-f4"); args.add_argument("-l4", default="f4")
args.add_argument("-f5"); args.add_argument("-l5", default="f5")
args.add_argument("-f6"); args.add_argument("-l6", default="f6")
args.add_argument("--filename", default=None)
args.add_argument("--start-i", type=int, default=1)
args.add_argument("--end-i", type=int, default=None)
args = args.parse_args()

LABELS = [args.l0, args.l1, args.l2, args.l3, args.l4, args.l5, args.l6]

data_all = []

if args.f0 is not None:
    data_all.append(read_json(args.f0))
if args.f1 is not None:
    data_all.append(read_json(args.f1))
if args.f2 is not None:
    data_all.append(read_json(args.f2))
if args.f3 is not None:
    data_all.append(read_json(args.f3))
if args.f4 is not None:
    data_all.append(read_json(args.f4))
if args.f5 is not None:
    data_all.append(read_json(args.f5))
if args.f6 is not None:
    data_all.append(read_json(args.f6))

data_all = [aggregate_epochs(data_fx[args.start_i:args.end_i]) for data_fx in data_all]
print(*[len(data_fx) for data_fx in data_all])

if len(data_all) <= 4:
    fig = plt.figure(figsize=(5, 4.7))
    legend_anchor = (0.5, 1.3)
elif len(data_all) == 5:
    # TODO not adapted
    fig = plt.figure(figsize=(5, 4.9))
    legend_anchor = (0.5, 1.42)
elif len(data_all) == 6:
    # TODO not adapted
    fig = plt.figure(figsize=(5, 5.4))
    legend_anchor = (0.5, 1.45)
elif len(data_all) == 7:
    fig = plt.figure(figsize=(5, 5.0))
    legend_anchor = (0.5, 1.35)

ax1 = fig.gca()
ax2 = ax1.twinx()

XTICKS = [
    x + args.start_i
    for x in range(max([len(data_fx) for data_fx in data_all]))
]

print(*[len(data_fx) for data_fx in data_all])

# fake call for the legend
ax1.plot(
    XTICKS[0],
    data_all[0][0]["train_loss"],
    label=f"Train Loss",
    linestyle=":",
    alpha=1,
    color="tab:grey"
)



for i, (data_fx, label) in enumerate(zip(data_all, LABELS)):
    ax1.plot(
        XTICKS[:len(data_fx)],
        [x["train_loss"] for x in data_fx],
        # label=f"Train Loss{label}",
        linestyle=":",
        alpha=0.6,
    )
    ax2.plot(
        XTICKS[:len(data_fx)],
        [x["dev_pp"] for x in data_fx],
        label=f"Dev PP{label}",
        linestyle="-",
        # marker=".",
        alpha=0.8,
    )
    ax2.scatter(
        XTICKS[:len(data_fx)],
        [x["dev_pp"] for x in data_fx],
        marker=".",
        alpha=0.5,
    )
ax1.set_ylabel("Train loss")
ax1.set_xlabel("Step | Epoch")


ax2.set_ylabel("Dev Perplexity")

fig.legend(
    loc="upper center",
    bbox_to_anchor=legend_anchor,
    bbox_transform=ax1.transAxes,
    ncol=2,
    columnspacing=1.0,
    handleheight=1.5
)

# plt.legend()
if len(data_all) == 4:
    plt.tight_layout(rect=(0, 0, 1, 0.8), pad=0)
# TODO not adapted
elif len(data_all) == 5:
    plt.tight_layout(rect=(0, 0, 1, 0.72), pad=0)
# TODO not adapted
elif len(data_all) == 6:
    plt.tight_layout(rect=(0, 0, 1, 0.7), pad=0)
elif len(data_all) == 7:
    plt.tight_layout(rect=(0, 0, 1, 0.77), pad=0)

if args.filename:
    plt.savefig(args.filename)
plt.show()
