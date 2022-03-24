#!/usr/bin/env python3

import sys
sys.path.append("src")
from argparse import ArgumentParser
from misc.utils import read_json
import matplotlib.pyplot as plt

args = ArgumentParser()
args.add_argument("-f0")
args.add_argument("-f1")
args.add_argument("-f2")
args.add_argument("-f3")
args.add_argument("-l0", default="f0")
args.add_argument("-l1", default="f1")
args.add_argument("-l2", default="f2")
args.add_argument("-l3", default="f3")
args = args.parse_args()

LABELS = [args.l0, args.l1, args.l2, args.l3]

data_all = []

if args.f0 is not None:
    data_all.append(read_json(args.f0)[1:])
if args.f1 is not None:
    data_all.append(read_json(args.f1)[1:])
if args.f2 is not None:
    data_all.append(read_json(args.f2)[1:])
if args.f3 is not None:
    data_all.append(read_json(args.f3)[1:])

fig = plt.figure(figsize=(8, 6))
ax1 = fig.gca()
ax2 = ax1.twinx()
ax3 = ax1.twinx()

XTICKS = [x + 1 for x in range(max([len(data_fx) for data_fx in data_all]))]
epochticks = []
prev_epoch = -1
for i, x in enumerate(data_all[0]):
    if x["epoch"] > prev_epoch:
        prev_epoch = x["epoch"]
        epochticks.append(i + 1)

print(*[len(data_fx) for data_fx in data_all])

# fake epoch ticks
ax3.scatter(
    epochticks,
    [0 for _ in epochticks],
    marker="|", color="black",
    s=1000,
)
ax3.set_ylim(0, 1)
ax3.get_yaxis().set_visible(False)

for i, (data_fx, label) in enumerate(zip(data_all, LABELS)):
    ax1.plot(
        XTICKS[:len(data_fx)],
        [x["train_loss"] for x in data_fx],
        label=f"Train Loss {label}",
        linestyle=":",
    )
    ax2.plot(
        XTICKS[:len(data_fx)],
        [x["dev_pp"] for x in data_fx],
        label=f"Dev PP {label}",
        linestyle="-",
        marker=".", markersize=5,
    )
ax1.set_ylabel("Train loss")
ax1.set_xlabel("Step | Epoch")


ax2.set_ylabel("Dev Perplexity")

fig.legend(
    loc="upper left",
    bbox_to_anchor=(-0.03, 1.18),
    bbox_transform=ax1.transAxes,
    ncol=4,
)
# l1+l2, lab1+lab2)

# plt.legend()
plt.tight_layout(rect=(0, 0, 1, 0.88))
plt.show()
