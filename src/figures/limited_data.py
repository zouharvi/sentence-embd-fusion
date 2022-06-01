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

XTICKS_Y = [1000, 2200, 4700, 9363, 17900, 32800, 58181, 100000]
XTICKS_LABELS = [f"{y/1000:.1f}k" for y in XTICKS_Y]
XTICKS_X = list(range(len(XTICKS_Y)))
PLOTARGS = {"ms": 8}

plt.xscale('log')
plt.plot(
    XTICKS_Y, data_f0+[17]*3,
    label="No fusion",
    marker=MARKERS[0],
    **PLOTARGS,
)
plt.plot(
    XTICKS_Y, data_f1+[17]*3,
    label="Concatenate final",
    marker=MARKERS[1],
    **PLOTARGS,
)
plt.plot(
    XTICKS_Y, data_f3+[17]*3,
    label="Multiply final",
    marker=MARKERS[2],
    **PLOTARGS,
)
plt.plot(
    XTICKS_Y, data_f5+[17]*3,
    label="Hidden state",
    marker=MARKERS[3],
    **PLOTARGS,
)
plt.minorticks_off()
plt.xticks(XTICKS_Y, XTICKS_LABELS)

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



# def powspace(start, stop, power, num):
#     start = np.power(start, 1/float(power))
#     stop = np.power(stop, 1/float(power))
#     return np.power( np.linspace(start, stop, num=num), power) 
# XTICKS_Y = [1000, 1900, 3400, 5900, 10100, 16700, 26900, 42500, 65800, 100000]
