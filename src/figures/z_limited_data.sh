#!/usr/bin/env bash

# random files for now
./src/figures/limited_data.py \
    --f0 \
        computed/v1/bert_cls-bluedog-f0.json computed/v1/bert_cls-bluedog-f0.json \
        computed/v1/bert_cls-bluedog-f0.json computed/v1/bert_cls-outjet-f4.json \
        computed/v1/bert_cls-bluedog-f0.json \
    --f1 \
        computed/bert_avg-wankle-f1.json computed/bert_avg-wankle-f1.json \
        computed/bert_avg-wankle-f1.json computed/v1/bert_cls-outjet-f4.json \
        computed/bert_avg-wankle-f1.json \
    --f3 \
        computed/v1/bert_cls-bluedog-f0.json computed/v1/bert_cls-bluedog-f0.json \
        computed/v1/bert_cls-bluedog-f0.json computed/v1/bert_cls-outjet-f4.json \
        computed/v1/bert_cls-bluedog-f0.json \
    --f5 \
        computed/bert_avg-wankle-f1.json computed/bert_avg-wankle-f1.json \
        computed/bert_avg-wankle-f1.json computed/v1/bert_cls-outjet-f4.json \
        computed/bert_avg-wankle-f1.json 