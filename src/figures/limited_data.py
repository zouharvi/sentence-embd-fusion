#!/usr/bin/env python3

import matplotlib.pyplot as plt
import sys
sys.path.append("src")
from misc.utils import read_json
from argparse import ArgumentParser
from fig_utils import *

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

fig = plt.figure(figsize=(6.5, 4))
XTICKS_LABELS = [5, 10, 25, 50, 100]
XTICKS = list(range(len(XTICKS_LABELS)))
PLOTARGS = {"ms": 8}

plt.plot(
    XTICKS, data_f0,
    label="No fusion",
    marker=MARKERS[0],
    **PLOTARGS,
)
plt.plot(
    XTICKS, data_f1,
    label="Concatenate final",
    marker=MARKERS[1],
    **PLOTARGS,
)
plt.plot(
    XTICKS, data_f3,
    label="Multiply final",
    marker=MARKERS[2],
    **PLOTARGS,
)
plt.plot(
    XTICKS, data_f5,
    label="Hidden state",
    marker=MARKERS[3],
    **PLOTARGS,
)
plt.xticks(XTICKS, [f"{x}k" for x in XTICKS_LABELS])

plt.ylabel("Dev Perplexity")
plt.xlabel("Training data")

plt.legend(
    loc="upper left",
    bbox_to_anchor=(0.17, 1.23),
    ncol=2,
)
plt.tight_layout(rect=(0, 0, 1, 1.01), pad=0.3)
plt.savefig("figures/limited_data.pdf")
plt.show()
