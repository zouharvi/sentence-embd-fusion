#!/usr/bin/env bash

./src/figures/intro_multiple_f.py \
    -f0 ./computed/bert-grum-f0.json -l0 ": No fusion" \
    -f1 ./computed/bert-bardel-f1.json -l1 ": Concat final" \
    -f2 ./computed/bert-technophile-f2.json -l2 ": Add final" \
    -f3 ./computed/bert-vacuum-f3.json -l3 ": Multiply final" \
    -f4 ./computed/bert-outjet-f4.json -l4 ": \$h_0\$" \
    -f5 ./computed/bert-guffle-f5.json -l5 ": \$c_0\$" \
    -f6 ./computed/bert-thamin-f6.json -l6 ": \$h_0, c_0\$" \
    --filename computed/fusions.pdf --start-i 1

    # -f1 ./computed/bert-wettissue-f1.json -l2 "No fusion"