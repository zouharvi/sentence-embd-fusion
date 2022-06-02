#!/usr/bin/env bash

# random files for now
./src/figures/limited_data.py \
    --f0 \
        computed/bert_cls-bluedog-f0.json computed/bert_cls-bluedog-f0.json \
        computed/bert_cls-bluedog-f0.json computed/bert_cls-outjet-f4.json \
        computed/bert_cls-truedog-f0.json \
    --f1 \
        computed/bert_cls-clover_5k-f1.json \
        computed/bert_cls-clover_8k-f1.json \
        computed/bert_cls-clover_13k-f1.json \
        computed/bert_cls-clover_20k-f1.json \
        computed/bert_cls-clover_31k-f1.json \
        computed/bert_cls-clover_46k-f1.json \
        computed/bert_cls-clover_68k-f1.json \
        computed/bert_cls-truetit-f1.json \
    --f3 \
        computed/bert_cls-transom_5k-f4.json \
        computed/bert_cls-tesera_5k-f5.json \
        computed/bert_cls-truemin-f6.json computed/bert_cls-truephile-f2.json \
        computed/bert_cls-outjet-f4.json \
    --f6 \
        computed/bert_cls-kora_5k-f6.json \
        computed/bert_cls-kora_8k-f6.json \
        computed/bert_cls-kora_13k-f6.json \
        computed/bert_cls-kora_20k-f6.json \
        computed/bert_cls-kora_31k-f6.json \
        computed/bert_cls-kora_46k-f6.json \
        computed/bert_cls-kora_68k-f6.json \
        computed/bert_cls-truemin-f6.json