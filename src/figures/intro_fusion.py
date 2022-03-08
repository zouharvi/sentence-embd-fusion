#!/usr/bin/env python3

import matplotlib.pyplot as plt
import sys
sys.path.append("src")
from misc.utils import read_json

data_f0 = read_json("computed/bert-10000-f0.json")
data_f1 = read_json("computed/bert-10000-f1.json")

fig = plt.figure(figsize=(6, 4))
ax1 = fig.gca()
ax2 = ax1.twinx()

ax1.plot(
    [x["train_loss"] for x in data_f0],
    label="Train loss, no fusion",
)
ax1.plot(
    [x["train_loss"] for x in data_f1],
    label="Train loss, fusion",
)
ax1.set_ylabel("Train loss")
ax1.set_xlabel("Epoch")

ax2.plot(
    [x["dev_pp"] for x in data_f0],
    label="Dev PP, no fusion",
    linestyle=":"
)
ax2.plot(
    [x["dev_pp"] for x in data_f1],
    label="Dev PP, fusion",
    linestyle=":"
)
ax2.set_ylabel("Dev Perplexity")

fig.legend(
    loc="upper left",
    bbox_to_anchor=(0, 1.2),
    bbox_transform=ax1.transAxes,
    ncol=2,
)
# l1+l2, lab1+lab2)

# plt.legend()
plt.tight_layout(rect=(0, 0, 1, 0.9))
plt.show()
