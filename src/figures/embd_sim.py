#!/usr/bin/env python3

import matplotlib.pyplot as plt
import sys
sys.path.append("src")
from misc.utils import read_pickle, save_pickle
from argparse import ArgumentParser
from collections import defaultdict
import numpy as np
from tqdm import tqdm
import fig_utils


def l2(a, b):
    return np.sqrt(np.sum(np.square(a - b)))


def ip(a, b):
    return np.inner(a / np.linalg.norm(a), b / np.linalg.norm(b))


args = ArgumentParser()
args.add_argument("-d", "--data", default="/data/sef/bert_cls-100k-p.embd")
args.add_argument("-l", "--load", action="store_true")
args = args.parse_args()

if not args.load:
    # get only the embeddings
    data = [x[2] for x in read_pickle(args.data)]

    buckets_ip_whole = defaultdict(list)
    buckets_ip = defaultdict(list)

    for embd in tqdm(data):
        for i in range(1, len(embd)):
            buckets_ip[i].append(ip(embd[i - 1], embd[i]))
            buckets_ip_whole[i].append(ip(embd[i - 1], embd[-1]))

    save_pickle("computed/buckets_ip_whole.pkl", buckets_ip_whole)
    save_pickle("computed/buckets_ip.pkl", buckets_ip)
else:
    buckets_ip_whole = read_pickle("computed/buckets_ip_whole.pkl")
    buckets_ip = read_pickle("computed/buckets_ip.pkl")

LIMIT_X = 200
data_ip_whole = [
    (i, np.average(buckets_ip_whole[i]))
    for i in sorted(buckets_ip_whole.keys())
    if i <= LIMIT_X
]
data_ip = [
    (i, np.average(buckets_ip[i]))
    for i in sorted(buckets_ip.keys())
    if i <= LIMIT_X
]
data_count = [
    (i, len(buckets_ip[i]))
    for i in sorted(buckets_ip.keys())
    if i <= LIMIT_X
][::4]

print("last data_count", data_count[-1])

fig = plt.figure(figsize=(5, 3))
ax1 = fig.gca()
ax2 = ax1.twinx()
# ax3 = ax1.twinx()  # used for counts

ax1.plot()

ax1.set_xlabel("Prefix length (i)")
ax1.set_ylabel("Norm. IP similarity")
ax2.set_ylabel("Count")

ax1.plot(
    [x[0] for x in data_ip],
    [x[1] for x in data_ip],
    color="seagreen",
    # label="IP$(embd(w_{:i-1}), embd(w_{:i}))$",
    label="Sim. to previous embd.",
)
ax1.plot(
    [x[0] for x in data_ip_whole],
    [x[1] for x in data_ip_whole],
    color="cornflowerblue",
    # label="IP$(embd(w_{:i-1}), embd(w_{-1}))$",
    label="Sim. to whole embd.",
)

ax2.scatter(
    [x[0] for x in data_count],
    [x[1] for x in data_count],
    color="tab:gray",
    s=10,
    label="Vector count",
    alpha=0.6,
)

fig.legend(
    loc=(0.4, 0.5),
    # bbox_to_anchor=(0, 1.22),
    # bbox_transform=ax2.transAxes,
    # ncol=2,
)

plt.tight_layout(pad=0)
plt.savefig("computed/embd_sim.pdf")
plt.show()