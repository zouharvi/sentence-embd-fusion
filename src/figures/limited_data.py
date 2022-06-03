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
args.add_argument("--f2", nargs="+")
args.add_argument("--f3", nargs="+")
args.add_argument("--f6", nargs="+")
args = args.parse_args()

data_f0 = []
for f in args.f0:
    data_f0.append(min([x["dev_pp"] for x in read_json(f)]))
data_f1 = []
for f in args.f1:
    data_f1.append(min([x["dev_pp"] for x in read_json(f)]))
data_f2 = []
for f in args.f2:
    data_f2.append(min([x["dev_pp"] for x in read_json(f)]))
data_f3 = []
for f in args.f3:
    data_f3.append(min([x["dev_pp"] for x in read_json(f)]))
data_f6 = []
for f in args.f6:
    data_f6.append(min([x["dev_pp"] for x in read_json(f)]))

fig = plt.figure(figsize=(6.5, 4))

XTICKS_Y = [5000, 8000, 13000, 20000, 31000, 46000, 68000, 100000]
XTICKS_LABELS = [f"{y/1000:.1f}k" for y in XTICKS_Y]
XTICKS_X = list(range(len(XTICKS_Y)))
PLOTARGS = {"ms": 8}

plt.xscale('log')
plt.plot(
    XTICKS_Y, data_f0,
    label="No fusion",
    marker=MARKERS[0],
    **PLOTARGS,
)
plt.plot(
    XTICKS_Y, data_f1,
    label="Concatenate final",
    marker=MARKERS[1],
    **PLOTARGS,
)
plt.plot(
    XTICKS_Y, data_f2,
    label="Add final",
    marker=MARKERS[2],
    **PLOTARGS,
)
plt.plot(
    XTICKS_Y, data_f3,
    label="Multiply final",
    marker=MARKERS[3],
    **PLOTARGS,
)
plt.plot(
    XTICKS_Y, data_f6,
    label="Hidden state",
    marker=MARKERS[4],
    **PLOTARGS,
)
plt.minorticks_off()
plt.xticks(XTICKS_Y, XTICKS_LABELS)

plt.ylabel("Dev Perplexity")
plt.xlabel("Training data")

plt.tight_layout(rect=(0, 0, 1, 0.80), pad=0)
plt.legend(
    loc="upper left",
    bbox_to_anchor=(0.17, 1.3),
    ncol=2,
)
plt.savefig("figures/limited_data.pdf")
plt.show()

# def powspace(start, stop, power, num):
#     start = np.power(start, 1/float(power))
#     stop = np.power(stop, 1/float(power))
#     return np.power( np.linspace(start, stop, num=num), power) 
# XTICKS_Y = [1000, 1900, 3400, 5900, 10100, 16700, 26900, 42500, 65800, 100000]
