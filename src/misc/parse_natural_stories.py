#!/usr/bin/env python3

from utils import save_pickle
from tqdm import tqdm

with open("data/processed_RTs.tsv", "r") as f:
    data = [l.strip().split("\t") for l in f.readlines()[1:]]
    data = [(l[6], l[8]) for l in data]


prev_token = None
sents = []
sent_w = []
sent_p = []

for l in tqdm(data):
    if l[0] == prev_token:
        continue
    prev_token = l[0]
    sent_w.append(l[0])
    sent_p.append(float(l[1]))
    if l[0].endswith(".") or l[0].endswith("?"):
        sents.append((sent_w, sent_p))
        sent_w = []
        sent_p = []

print(len(sents), "sentences in total")
save_pickle("data/natural_stories.pkl", sents)