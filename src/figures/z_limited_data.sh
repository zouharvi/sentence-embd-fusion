#!/usr/bin/env bash

# random files for now
./src/figures/limited_data.py \
    --f0 \
        computed/bert_cls-bluedog-f0.json computed/bert_cls-bluedog-f0.json \
        computed/bert_cls-bluedog-f0.json computed/bert_cls-outjet-f4.json \
        computed/bert_cls-truedog-f0.json \
    --f1 \
        computed/bert_avg-wankle-f1.json computed/bert_avg-wankle-f1.json \
        computed/bert_avg-wankle-f1.json computed/bert_cls-outjet-f4.json \
        computed/bert_cls-truetit-f1.json \
    --f3 \
        computed/bert_cls-bluedog-f0.json computed/bert_cls-bluedog-f0.json \
        computed/bert_cls-truemin-f6.json computed/bert_cls-truephile-f2.json \
        computed/bert_cls-outjet-f4.json \
    --f5 \
        computed/bert_cls-vacuum-f3.json computed/bert_cls-truemin-f6.json \
        computed/bert_cls-vacuum-f3.json computed/bert_cls-technohpile-f2.json \
        computed/bert_cls-vacuum-f3.json 