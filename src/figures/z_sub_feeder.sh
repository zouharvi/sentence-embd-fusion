#!/usr/bin/env bash

# random files for now
./src/figures/sub_feeders.py \
    --subl-k 0.5 0.75 \
    --subl computed/v1/bert_cls-bluedog-f0.json computed/v1/bert_cls-bluedog-f0.json \
    --subr-k 0.5 0.75 0.95 \
    --subr computed/v1/bert_cls-guffle-f5.json computed/bert_avg-wankle-f1.json computed/v1/bert_cls-outjet-f4.json \
    --pp-f0 15 \
    --pp-f1 16