#!/usr/bin/env bash

./src/figures/intro_multiple_f.py \
    -f0 ./computed/bert_cls-bluedog-f0.json -l0 ": No fusion" \
    -f1 ./computed/bert_cls-petit-f1.json -l1 ": No dropout" \
    -f2 ./computed/bert_cls-skewedapple_1-f1.json -l2 ": No$\rightarrow\$full dropout" \
    -f3 ./computed/bert_cls-sadmate_1-f1.json -l3 ": Full$\rightarrow\$no dropout" \
    --filename computed/wean_off.pdf --start-i 5 --end-i 240
    # -f1 ./computed/bert-wettissue-f1.json -l2 "No fusion"
    
    # 0.0, 0.25, 0.5, 0.75, 1.0
    # 1.0, 0.75, 0.5, 0.25, 0.0