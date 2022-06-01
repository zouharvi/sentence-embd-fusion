#!/usr/bin/env bash

./src/figures/multiple_f.py \
    -f0 ./computed/bert_cls-truedog-f0.json -l0 ": No fusion" \
    -f1 ./computed/bert_cls-truetit-f1.json -l1 ": Concat final" \
    -f2 ./computed/bert_cls-truephile-f2.json -l2 ": Add final" \
    -f3 ./computed/bert_cls-truecuum-f3.json -l3 ": Multiply final" \
    -f4 ./computed/bert_cls-truemin-f6.json -l4 ": \$h_0, c_0\$" \
    --filename figures/fusions.pdf --start-i 10 --legend-y 0.01
    # -f4 ./computed/v1/bert_cls-outjet-f4.json -l4 ": \$h_0\$" \
    # -f5 ./computed/v1/bert_cls-guffle-f5.json -l5 ": \$c_0\$" \

    # -f1 ./computed/bert-wettissue-f1.json -l2 "No fusion"