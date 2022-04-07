#!/usr/bin/env bash

./src/figures/intro_multiple_f.py \
    -f0 ./computed/bert-grum-f0.json -l0 ": No fusion" \
    -f1 ./computed/bert-bardel-f1.json -l1 ": Concat final" \
    -f2 ./computed/bert-technophile-f2.json -l2 ": Add final" \
    -f3 ./computed/bert-vacuum-f3.json -l3 ": Multiply final" \
    --filename computed/fusions.pdf --start-i 5
    # -f1 ./computed/bert-wettissue-f1.json -l2 "No fusion"
    
    # 0.0, 0.25, 0.5, 0.75, 1.0
    # 1.0, 0.75, 0.5, 0.25, 0.0