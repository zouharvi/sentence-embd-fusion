#!/usr/bin/env python3

import matplotlib.pyplot as plt
import sys
sys.path.append("src")
from misc.utils import read_json
from argparse import ArgumentParser
import fig_utils

args = ArgumentParser()
args.add_argument("-f0")
args.add_argument("-f1")
args = args.parse_args()

data_f0 = read_json(args.f0)[1:]
data_f1 = read_json(args.f1)[1:]

fig = plt.figure(figsize=(6, 4))
ax1 = fig.gca()
ax2 = ax1.twinx()
ax3 = ax1.twinx()

XTICKS = [x+1 for x in range(max(len(data_f0),len(data_f1)))]
epochticks = []
prev_epoch = -1
for i, x in enumerate(data_f0):
    if x["epoch"] > prev_epoch:
        prev_epoch = x["epoch"]
        epochticks.append(i+1)
        
print(len(data_f0), len(data_f1))

# fake epoch ticks
ax3.scatter(
    epochticks,
    [0 for _ in epochticks],
    marker="|", color="black",
    s=1000,
)
ax3.set_ylim(0,1)
ax3.get_yaxis().set_visible(False)

ax1.plot(
    XTICKS[:len(data_f0)],
    [x["train_loss"] for x in data_f0],
    label="Train loss",
    linestyle=":",
)
ax1.plot(
    XTICKS[:len(data_f1)],
    [x["train_loss"] for x in data_f1],
    label="Train loss, $\\bf{fusion}$",
    linestyle=":",
)
ax1.set_ylabel("Train loss")
ax1.set_xlabel("Step | Epoch")

ax2.plot(
    XTICKS[:len(data_f0)],
    [x["dev_pp"] for x in data_f0],
    label="Dev PP",
    linestyle="-",
    marker=".", markersize=5,
)
ax2.plot(
    XTICKS[:len(data_f1)],
    [x["dev_pp"] for x in data_f1],
    label="Dev PP, $\\bf{fusion}$",
    linestyle="-",
    marker=".", markersize=5,
)
ax2.set_ylabel("Dev Perplexity")

fig.legend(
    loc="upper left",
    bbox_to_anchor=(0, 1.22),
    bbox_transform=ax1.transAxes,
    ncol=2,
)
# l1+l2, lab1+lab2)

# plt.legend()
plt.tight_layout(rect=(0, 0, 1, 0.88))
plt.show()
