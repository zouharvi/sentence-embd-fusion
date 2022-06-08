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
ax1 = fig.gca()

XTICKS_Y = [5000, 8000, 13000, 20000, 31000, 46000, 68000, 100000]
XTICKS_LABELS = [f"{y/1000:.0f}k" for y in XTICKS_Y]
XTICKS_X = list(range(len(XTICKS_Y)))
PLOTARGS = {"ms": 8}


def plot_to_axis(ax, sl):
    ax.set_xscale('log')
    ax.plot(
        XTICKS_Y[sl], data_f0[sl],
        label="No fusion",
        marker=MARKERS[0],
        **PLOTARGS,
    )
    ax.plot(
        XTICKS_Y[sl], data_f1[sl],
        label="Concatenate final",
        marker=MARKERS[1],
        **PLOTARGS,
    )
    ax.plot(
        XTICKS_Y[sl], data_f2[sl],
        label="Add final",
        marker=MARKERS[2],
        **PLOTARGS,
    )
    ax.plot(
        XTICKS_Y[sl], data_f3[sl],
        label="Multiply final",
        marker=MARKERS[3],
        **PLOTARGS,
    )
    ax.plot(
        XTICKS_Y[sl], data_f6[sl],
        label="Hidden state",
        marker=MARKERS[4],
        **PLOTARGS,
    )
    ax1.minorticks_off()


plot_to_axis(ax1, slice(None, None))
ax1.set_xticks(XTICKS_Y, XTICKS_LABELS)

ax1.set_ylabel("Dev Perplexity")
ax1.set_xlabel("Training data")

ax2 = ax1.inset_axes([0.931, 0.35, 0.05, 0.6])
ax2.set_xscale('log')
plot_to_axis(ax2, slice(-1, None))
ax2.get_xaxis().set_visible(False)
# fake limits for inset zoom
ax2.set_xlim(XTICKS_Y[-1] - 7000, XTICKS_Y[-1] + 8000)
ax2.set_ylim(14.6, 18)
ax1.indicate_inset_zoom(ax2, edgecolor="black")
# true limits
ax2.set_ylim(15.6, 17)
ax2.set_yticks([16, 17])

ax3 = ax1.inset_axes([0.814, 0.35, 0.05, 0.6])
ax3.set_xscale('log')
plot_to_axis(ax3, slice(-2, -1))
ax3.get_xaxis().set_visible(False)
# fake limits for inset zoom
ax3.set_xlim(XTICKS_Y[-2] - 5000, XTICKS_Y[-2] + 6000)
ax3.set_ylim(16.5, 20.5)
ax1.indicate_inset_zoom(ax3, edgecolor="black")
# true limits
ax3.set_ylim(17, 20)

ax4 = ax1.inset_axes([0.694, 0.35, 0.05, 0.6])
ax4.set_xscale('log')
plot_to_axis(ax4, slice(-3, -2))
ax4.get_xaxis().set_visible(False)
# fake limits for inset zoom
ax4.set_xlim(XTICKS_Y[-3] - 3700, XTICKS_Y[-3] + 4000)
ax4.set_ylim(18, 22)
ax1.indicate_inset_zoom(ax4, edgecolor="black")
# true limits
ax4.set_ylim(19, 22)
ax4.set_yticks([19, 20, 21])


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
