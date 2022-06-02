#!/usr/bin/env bash

# random files for now
./src/figures/sub_feeders.py \
    --sub-k 0 0.25 0.5 0.75 1.0 \
    --subl \
        computed/bert_cls-truetit-f1.json "computed/bert_cls-nimonic_l25-f1.json" \
        "computed/bert_cls-nimonic_l5-f1.json" "computed/bert_cls-nimonic_l75-f1.json" \
        computed/bert_cls-truedog-f0.json \
    --subr \
        computed/bert_cls-truedog-f0.json "computed/bert_cls-nimonic_r25-f1.json" \
        "computed/bert_cls-nimonic_r5-f1.json" "computed/bert_cls-nimonic_r75-f1.json" \
        computed/bert_cls-truetit-f1.json \