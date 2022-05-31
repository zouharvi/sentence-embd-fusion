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
args.add_argument("-d", "--data", default="/data/sef/bert_cls-110k-p.embd")
args.add_argument("-dl", "--data-subl", type=list, nargs="+", default=[
    "/data/sef/bert_cls_(subl0.25)-110k-p.embd",
    "/data/sef/bert_cls_(subl0.5)-110k-p.embd",
    "/data/sef/bert_cls_(subl0.75)-110k-p.embd",
])
args.add_argument("-dr", "--data-subr", type=list, nargs="+", default=[
    "/data/sef/bert_cls_(subr0.25)-110k-p.embd",
    "/data/sef/bert_cls_(subr0.5)-110k-p.embd",
    "/data/sef/bert_cls_(subr0.75)-110k-p.embd",
])
args.add_argument("-l", "--load", action="store_true")
args.add_argument("-ck", "--compute-ks", action="store_true")
args = args.parse_args()

if not args.load:
    print("Loading data")
    # get only the embeddings of training data
    data = [x[2] for x in read_pickle(args.data)[:100000]]

    buckets_whole = defaultdict(list)
    buckets_prev = defaultdict(list)

    print("Computing standard pass")
    for embd in tqdm(data):
        for i in range(1, len(embd)):
            buckets_prev[i].append(ip(embd[i - 1], embd[i]))
            buckets_whole[i].append(ip(embd[i - 1], embd[-1]))

    if args.compute_ks:
        KS = [0.25, 0.5, 0.75]

        print("Computing subr")
        sim_sub = {}
        for f, k in zip(args.data_subr, KS):
            print(f"Loading subr{k}")
            # get only the embeddings of training data
            data_s = [x[2] for x in read_pickle(f)[:100000]]
            sim = []
            for embd, embd_s in tqdm(zip(data, data_s), total=len(data)):
                for i in range(0, len(embd)):
                    sim.append(ip(embd[i], embd_s[i]))
            sim_sub[k] = np.average(sim)
        print("SIM_SUBR = ", end="")
        print(sim_sub)

        print("Computing subl")
        sim_sub = {}
        for f, k in zip(args.data_subl, KS):
            print(f"Loading subl{k}")
            # get only the embeddings of training data
            data_s = [x[2] for x in read_pickle(f)[:100000]]
            sim = []
            for embd, embd_s in tqdm(zip(data, data_s), total=len(data)):
                for i in range(0, len(embd)):
                    sim.append(ip(embd[i], embd_s[i]))
            sim_sub[k] = np.average(sim)
        print("SIM_SUBL = ", end="")
        print(sim_sub)

    save_pickle("computed/buckets_all.pkl", (buckets_whole, buckets_prev))
else:
    buckets_whole, buckets_prev = read_pickle("computed/buckets_all.pkl")

# manual crop by sentence length
LIMIT_X = 200
data_ip_whole = [
    (i, np.average(buckets_whole[i]))
    for i in sorted(buckets_whole.keys())
    if i <= LIMIT_X
]
data_ip = [
    (i, np.average(buckets_prev[i]))
    for i in sorted(buckets_prev.keys())
    if i <= LIMIT_X
]
data_count = [
    (i, len(buckets_prev[i]))
    for i in sorted(buckets_prev.keys())
    if i <= LIMIT_X
][::4]

print("last data_count", data_count[-1])

fig = plt.figure(figsize=(5.9, 4))
ax1 = fig.gca()
ax2 = ax1.twinx()

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
    loc="upper center",
    bbox_to_anchor=(0.52, 1.14),
    bbox_transform=ax1.transAxes,
    ncol=3,
)

plt.tight_layout(rect=(0, 0, 1, 0.9), pad=0)
plt.savefig("figures/embd_sim.pdf")
plt.show()