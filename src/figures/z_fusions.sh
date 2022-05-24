#!/usr/bin/env bash

./src/figures/intro_multiple_f.py \
    -f0 ./computed/v1/bert_cls-bluedog-f0.json -l0 ": No fusion" \
    -f1 ./computed/v1/bert_cls-petit-f1.json -l1 ": Concat final" \
    -f2 ./computed/v1/bert_cls-technophile-f2.json -l2 ": Add final" \
    -f3 ./computed/v1/bert_cls-vacuum-f3.json -l3 ": Multiply final" \
    -f4 ./computed/v1/bert_cls-thamin-f6.json -l4 ": \$h_0, c_0\$" \
    --filename computed/fusions.pdf --start-i 10 
    # -f4 ./computed/v1/bert_cls-outjet-f4.json -l4 ": \$h_0\$" \
    # -f5 ./computed/v1/bert_cls-guffle-f5.json -l5 ": \$c_0\$" \

    # -f1 ./computed/bert-wettissue-f1.json -l2 "No fusion"