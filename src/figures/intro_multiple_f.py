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

ARGS_LABELS = [args.l0, args.l1, args.l2, args.l3, args.l4, args.l5, args.l6]
ARGS_FILES = [args.f0, args.f1, args.f2, args.f3, args.f4, args.f5, args.f6]
data_all = []
for f in ARGS_FILES:
    if f is not None:
        data_all.append(read_json(f))

data_all = [aggregate_epochs(data_fx[args.start_i:args.end_i]) for data_fx in data_all]
print(*[len(data_fx) for data_fx in data_all])

fig = plt.figure(figsize=(7, 5.0))


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


for i, (data_fx, label) in enumerate(zip(data_all, ARGS_LABELS)):
    # train loss
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
        alpha=0.7,
    )
    # only every 10th marker to clean up the graph
    ax2.scatter(
        XTICKS[:len(data_fx):10],
        [x["dev_pp"] for x in data_fx][::10],
        marker=".",
        alpha=0.8,
    )
ax1.set_ylabel("Train loss")
ax1.set_xlabel("Step | Epoch")


ax2.set_ylabel("Dev Perplexity")

fig.legend(
    loc="upper center",
    bbox_to_anchor=(0.5, 1.25),
    bbox_transform=ax1.transAxes,
    ncol=2,
)

plt.tight_layout(rect=(0, 0, 1, 0.82), pad=0)

if args.filename:
    plt.savefig(args.filename)
plt.show()
