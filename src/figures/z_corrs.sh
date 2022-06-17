#!/usr/bin/env bash

./src/figures/multiple_f.py \
    -f0 ./computed/bert_cls-whirl-f0.json -l0 "No fusion" \
    -f1 ./computed/bert_cls-whirl-f1.json -l1 "Concat final" \
    --filename figures/fusions.pdf --start-i 10 --end-i 400 --key-1 rt_corr --key-2 dev_pp
     #": \$h_0, c_0\$" \
    # -f4 ./computed/v1/bert_cls-outjet-f4.json -l4 ": \$h_0\$" \
    # -f5 ./computed/v1/bert_cls-guffle-f5.json -l5 ": \$c_0\$" \