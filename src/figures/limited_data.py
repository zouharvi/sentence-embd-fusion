#!/usr/bin/env python3

import matplotlib.pyplot as plt
import sys
sys.path.append("src")
from misc.utils import read_json
from argparse import ArgumentParser
import fig_utils

args = ArgumentParser()
args.add_argument("--f0", nargs="+")
args.add_argument("--f1", nargs="+")
args.add_argument("--f3", nargs="+")
args.add_argument("--f5", nargs="+")
args = args.parse_args()

data_f0 = []
for f in args.f0:
    data_f0.append(min([x["dev_pp"] for x in read_json(f)]))
data_f1 = []
for f in args.f1:
    data_f1.append(min([x["dev_pp"] for x in read_json(f)]))
data_f3 = []
for f in args.f3:
    data_f3.append(min([x["dev_pp"] for x in read_json(f)]))
data_f5 = []
for f in args.f5:
    data_f5.append(min([x["dev_pp"] for x in read_json(f)]))

fig = plt.figure(figsize=(6, 4))
XTICKS_LABELS = [5, 10, 25, 50, 100]
XTICKS = list(range(len(XTICKS_LABELS)))
PLOTARGS = {"ms": 10, "marker": "."}

plt.plot(
    XTICKS, data_f0,
    label="No fusion",
    **PLOTARGS,
)
plt.plot(
    XTICKS, data_f1,
    label="Concatenate final",
    **PLOTARGS,
)
plt.plot(
    XTICKS, data_f3,
    label="Multiply final",
    **PLOTARGS,
)
plt.plot(
    XTICKS, data_f5,
    label="Hidden state",
    **PLOTARGS,
)
plt.xticks(XTICKS, [f"{x}k" for x in XTICKS_LABELS])

plt.ylabel("Dev Perplexity")
plt.xlabel("Training data")

plt.legend(
    loc="upper left",
    bbox_to_anchor=(0.1, 1.3),
    ncol=2,
)
plt.tight_layout(rect=(0, 0, 1, 1.02), pad=0.3)
plt.savefig("computed/limited_data.pdf")
plt.show()
