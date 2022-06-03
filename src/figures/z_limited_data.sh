#!/usr/bin/env bash

# random files for now
./src/figures/limited_data.py \
    --f0 \
        computed/bert_cls-haemal_5k-f0.json \
        computed/bert_cls-haemal_8k-f0.json \
        computed/bert_cls-haemal_13k-f0.json \
        computed/bert_cls-haemal_20k-f0.json \
        computed/bert_cls-haemal_31k-f0.json \
        computed/bert_cls-haemal_46k-f0.json \
        computed/bert_cls-haemal_68k-f0.json \
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
    --f2 \
        computed/bert_cls-clover_5k-f1.json \
        computed/bert_cls-clover_8k-f1.json \
        computed/bert_cls-clover_13k-f1.json \
        computed/bert_cls-clover_20k-f1.json \
        computed/bert_cls-clover_31k-f1.json \
        computed/bert_cls-clover_46k-f1.json \
        computed/bert_cls-clover_68k-f1.json \
        computed/bert_cls-truetit-f1.json \
    --f3 \
        computed/bert_cls-voluble_5k-f3.json \
        computed/bert_cls-voluble_8k-f3.json \
        computed/bert_cls-voluble_13k-f3.json \
        computed/bert_cls-voluble_20k-f3.json \
        computed/bert_cls-voluble_31k-f3.json \
        computed/bert_cls-voluble_46k-f3.json \
        computed/bert_cls-voluble_68k-f3.json \
        computed/bert_cls-truecuum-f3.json \
    --f6 \
        computed/bert_cls-kora_5k-f6.json \
        computed/bert_cls-kora_8k-f6.json \
        computed/bert_cls-kora_13k-f6.json \
        computed/bert_cls-kora_20k-f6.json \
        computed/bert_cls-kora_31k-f6.json \
        computed/bert_cls-kora_46k-f6.json \
        computed/bert_cls-kora_68k-f6.json \
        computed/bert_cls-truemin-f6.json

        # computed/bert_cls-transom_5k-f4.json \
        # computed/bert_cls-tesera_5k-f5.json \
        