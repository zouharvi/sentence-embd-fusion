## TODO
- 

## Running/staged

(re)start|size|nickname|description|command|machine|status
-|-|-|-|-|-|-

## Finished
(re)start|size|nickname|description|command|machine|status
-|-|-|-|-|-|-
14 jun|100k+2|fountain|vocab shift|`./src/run_model_artefact.py -d /data/sef/bert_cls-110k.embd -d2 /data/sef/moctezuma_bert_cls-2.embd -nn fountain -mn bert_cls --encoder /data/sef/s110k-v8192.enc_pkl --prob-file computed/moctezuma_full_probs.json`|8|ok (stopped)
14 jun|100k+2|fountain|vocab shift|`./src/run_model_artefact.py -d /data/sef/bert_cls-110k-p.embd -d2 /data/sef/moctezuma_bert_cls-2-p.embd -nn fountain -mn bert_cls --encoder /data/sef/s110k-v8192.enc_pkl --prob-file computed/moctezuma_prefix_probs.json`|8|ok (stopped)
31 may - 5 jun|110k|truecuum|baseline check convergence|`./src/run_model_basic.py -d /data/sef/bert_cls-110k-p.embd -f 3 -nn truecuum -mn bert_cls -e 400 > runs/basic_truecuum.log`|16|killed, running, ok
5 jun|110k|truecuum|baseline clone (10 epochs behind)|`./src/run_model_basic.py -d /data/sef/bert_cls-110k-p.embd -f 3 -nn truecuum_2 -mn bert_cls -e 400 > runs/basic_truecuum_2.log`|13|ok
7 jun|110k|vastness_sbert_cls|spec artefact|`./src/run_model_basic.py -d "/data/sef/sbert_cls-110k-p.embd" -f 1 -nn vastness -mn sbert_cls > runs/vastness_sbert_cls.log`|15,13|died, ok
7 jun|110k|vastness_sbert_avg|spec artefact|`./src/run_model_basic.py -d "/data/sef/sbert_avg-110k-p.embd" -f 1 -nn vastness -mn sbert_avg > runs/vastness_sbert_avg.log`|12|ok
7 jun|110k|vastness_sbert_avg|spec artefact clone (4 epochs behind)|`./src/run_model_basic.py -d "/data/sef/sbert_avg-110k-p.embd" -f 1 -nn vastness_2 -mn sbert_avg > runs/vastness_sbert_avg_1.log`|8|ok (deleted)
7 jun|110k|vastness_count|spec artefact|`./src/run_model_basic.py -d "/data/sef/count-110k-p.embd" -f 1 -nn vastness -mn count > runs/vastness_count.log`|11|ok (stopped)
7 jun|110k|vastness_sbert_avg|spec artefact|`./src/run_model_basic.py -d "/data/sef/bert_cls_lr-110k-p.embd" -f 1 -nn vastness -mn bert_cls_lr > runs/vastness_bert_cls_lr.log`|13|ok (stopped)
7 jun|110k|vastness_tfidf|spec artefact|`./src/run_model_basic.py -d "/data/sef/tfidf-110k-p.embd" -f 1 -nn vastness -mn tfidf > runs/vastness_tfidf.log`|12|ok (stopped)
8 jun|110k|surety_bert_cls_lrcontext|artefact only|`./src/run_model_artefact.py -d "/data/sef/bert_cls_lr-110k-p.embd" -nn surety -mn bert_cls_lr > runs/art_surety_bert_cls_lr.log`|13|ok
7 jun|110k|vastness_bert_avg|spec artefact|`./src/run_model_basic.py -d "/data/sef/bert_avg-110k-p.embd" -f 1 -nn vastness -mn bert_avg > runs/vastness_bert_avg.log`|15|ok
7 jun|110k|vastness_bert_cls_f|spec artefact|`./src/run_model_basic.py -d "/data/sef/bert_cls-110k.embd" -f 1 -nn vastness -mn bert_cls_f > runs/vastness_bert_cls_f.log`|14|ok
7 jun|110k|bert_avg|embd|`./src/misc/embd.py -n 110000 -m bert --feeder lrcontext -p > runs/embd_bert_lrcontext.log`|10|ok
8 jun|110k|surety_bert_avg|artefact only|`./src/run_model_artefact.py -d "/data/sef/bert_avg-110k-p.embd" -nn surety -mn bert_avg > runs/art_surety_bert_avg.log`|10|ok (stopped)
8 jun|110k|surety_sbert_cls|artefact only|`./src/run_model_artefact.py -d "/data/sef/sbert_cls-110k-p.embd" -nn surety -mn sbert_cls > runs/art_surety_sbert_cls.log`|10|ok (stopped)
8 jun|110k|surety_sbert_avg|artefact only|`./src/run_model_artefact.py -d "/data/sef/sbert_avg-110k-p.embd" -nn surety -mn sbert_avg > runs/art_surety_sbert_avg.log`|13|ok (stopped)
3-5 jun|68+10k|xbox_68k|limited data|`./src/run_model_basic.py -d "/data/sef/bert_cls-110k-p.embd" -f 2 -nn xbox_68k -mn bert_cls -tn 68000 > runs/basic_xbox_68k.log`|10|killed, ok (stopped)
7 jun|110k|bert_avg|embd|`./src/misc/embd.py -n 110000 -m bert --type-out avg -p > runs/embd_bert_avg.log`|15|ok
7 jun|110k|sbert_cls|embd|`./src/misc/embd.py -n 110000 -m sbert --type-out cls -p > runs/embd_sbert_cls.log`|15|ok
7 jun|110k|sbert_avg|embd|`./src/misc/embd.py -n 110000 -m sbert --type-out avg -p > runs/embd_sbert_avg.log`|15|ok
7 jun|110k|surety_bert_cls_f|artefact only|`./src/run_model_artefact.py -d "/data/sef/bert_cls-110k.embd" -nn surety -mn bert_cls_f > runs/art_surety_bert_cls_f.log`|11|ok
7 jun|110k|surety_bert_cls|artefact only|`./src/run_model_artefact.py -d "/data/sef/bert_cls-110k-p.embd" -nn surety -mn bert_cls > runs/art_surety_bert_cls.log`|15|ok
7 jun|110k|surety_none|artefact only|`./src/run_model_artefact.py -d "/data/sef/none-110k-p.embd" -nn surety -mn none > runs/art_surety_none.log`|14|ok
7 jun|110k|surety_count|artefact only|`./src/run_model_artefact.py -d "/data/sef/count-110k-p.embd" -nn surety -mn count > runs/art_surety_count.log`|14|ok
7 jun|110k|surety_tfidf|artefact only|`./src/run_model_artefact.py -d "/data/sef/tfidf-110k-p.embd" -nn surety -mn tfidf > runs/art_surety_tfidf.log`|12|ok
7 jun|110k|bert_cls_f|embd|`./src/misc/embd.py -n 110000 -m bert --type-out cls > runs/embd_bert_cls_f.log`|14|ok
3-5 jun|46+10k|xbox_46k|limited data|`./src/run_model_basic.py -d "/data/sef/bert_cls-110k-p.embd" -f 2 -nn xbox_46k -mn bert_cls -tn 46000 > runs/basic_xbox_46k.log`|11|killed, ok
7 jun|110k|tfidf|embd|`./src/misc/embd.py -n 110000 -m tfidf -p > runs/embd_tfidf.log`|15|ok
7 jun|110k|none|embd|`./src/misc/embd.py -n 110000 -m none -p > runs/embd_none.log`|15|ok
7 jun|110k|count|embd|`./src/misc/embd.py -n 110000 -m count -p > runs/embd_count.log`|15|ok
3-5 jun|68+10k|voluble_68k|limited data|`./src/run_model_basic.py -d "/data/sef/bert_cls-110k-p.embd" -f 3 -nn voluble_68k -mn bert_cls -tn 68000 > runs/basic_voluble_68k.log`|14|killed, ok
3-5 jun|68+10k|haemal_68k|limited data|`./src/run_model_basic.py -d "/data/sef/bert_cls-110k-p.embd" -f 0 -nn haemal_68k -mn bert_cls -tn 68000 > runs/basic_haemal_68k.log`|15|killed, ok
3-5 jun|31+10k|xbox_31k|limited data|`./src/run_model_basic.py -d "/data/sef/bert_cls-110k-p.embd" -f 2 -nn xbox_31k -mn bert_cls -tn 31000 > runs/basic_xbox_31k.log`|12|killed, ok
3-5 jun|46+10k|voluble_46k|limited data|`./src/run_model_basic.py -d "/data/sef/bert_cls-110k-p.embd" -f 3 -nn voluble_46k -mn bert_cls -tn 46000 > runs/basic_voluble_46k.log`|14|killed, ok
3-5 jun|46+10k|haemal_46k|limited data|`./src/run_model_basic.py -d "/data/sef/bert_cls-110k-p.embd" -f 0 -nn haemal_46k -mn bert_cls -tn 46000 > runs/basic_haemal_46k.log`|15|killed, ok
3-5 jun|31+10k|voluble_31k|limited data|`./src/run_model_basic.py -d "/data/sef/bert_cls-110k-p.embd" -f 3 -nn voluble_31k -mn bert_cls -tn 31000 > runs/basic_voluble_31k.log`|15|killed, ok
3-5 jun|20+10k|xbox_20k|limited data|`./src/run_model_basic.py -d "/data/sef/bert_cls-110k-p.embd" -f 2 -nn xbox_20k -mn bert_cls -tn 20000 > runs/basic_xbox_20k.log`|13|killed, ok
3-5 jun|31+10k|haemal_31k|limited data|`./src/run_model_basic.py -d "/data/sef/bert_cls-110k-p.embd" -f 0 -nn haemal_31k -mn bert_cls -tn 31000 > runs/basic_haemal_31k.log`|16|killed, ok
3-5 jun|13+10k|xbox_13k|limited data|`./src/run_model_basic.py -d "/data/sef/bert_cls-110k-p.embd" -f 2 -nn xbox_13k -mn bert_cls -tn 13000 > runs/basic_xbox_13k.log`|13|killed, ok
3-5 jun|8+10k|xbox_8k|limited data|`./src/run_model_basic.py -d "/data/sef/bert_cls-110k-p.embd" -f 2 -nn xbox_8k -mn bert_cls -tn 8000 > runs/basic_xbox_8k.log`|13|killed, ok
3 jun|5+10k|xbox_5k|limited data|`./src/run_model_basic.py -d "/data/sef/bert_cls-110k-p.embd" -f 2 -nn xbox_5k -mn bert_cls -tn 5000 > runs/basic_xbox_5k.log`|8|ok (stopped)
3 jun|20+10k|haemal_20k|limited data|`./src/run_model_basic.py -d "/data/sef/bert_cls-110k-p.embd" -f 0 -nn haemal_20k -mn bert_cls -tn 20000 > runs/basic_haemal_20k.log`|10|ok (stopped)
3 jun|13+10k|haemal_13k|limited data|`./src/run_model_basic.py -d "/data/sef/bert_cls-110k-p.embd" -f 0 -nn haemal_13k -mn bert_cls -tn 13000 > runs/basic_haemal_13k.log`|10|ok (stopped)
3 jun|8+10k|haemal_8k|limited data|`./src/run_model_basic.py -d "/data/sef/bert_cls-110k-p.embd" -f 0 -nn haemal_8k -mn bert_cls -tn 8000 > runs/basic_haemal_8k.log`|8|ok
3 jun|20+10k|voluble_20k|limited data|`./src/run_model_basic.py -d "/data/sef/bert_cls-110k-p.embd" -f 3 -nn voluble_20k -mn bert_cls -tn 20000 > runs/basic_voluble_20k.log`|15|ok
1 jun|68+10k|clover_68k|limited data|`./src/run_model_basic.py -d "/data/sef/bert_cls-110k-p.embd" -f 1 -nn clover_68k -mn bert_cls -tn 68000 > runs/basic_clover_68k.log`|8|ok (Stopped)
2 jun|68+10k|kora_68k|limited data|`./src/run_model_basic.py -d "/data/sef/bert_cls-110k-p.embd" -f 6 -nn kora_68k -mn bert_cls -tn 68000 > runs/basic_kora_68k.log`|13|ok (stopped)
3 jun|5+10k|haemal_5k|limited data|`./src/run_model_basic.py -d "/data/sef/bert_cls-110k-p.embd" -f 0 -nn haemal_5k -mn bert_cls -tn 5000 > runs/basic_haemal_5k.log`|8|ok
3 jun|5+10k|voluble_5k|limited data|`./src/run_model_basic.py -d "/data/sef/bert_cls-110k-p.embd" -f 3 -nn voluble_5k -mn bert_cls -tn 5000 > runs/basic_voluble_5k.log`|13|ok
3 jun|8+10k|voluble_8k|limited data|`./src/run_model_basic.py -d "/data/sef/bert_cls-110k-p.embd" -f 3 -nn voluble_8k -mn bert_cls -tn 8000 > runs/basic_voluble_8k.log`|13|ok
3 jun|13+10k|voluble_13k|limited data|`./src/run_model_basic.py -d "/data/sef/bert_cls-110k-p.embd" -f 3 -nn voluble_13k -mn bert_cls -tn 13000 > runs/basic_voluble_13k.log`|15|ok
31 may|110k|truemin|baseline|`./src/run_model_basic.py -d /data/sef/bert_cls-110k-p.embd -f 6 -nn truemin -mn bert_cls > runs/basic_truemin.log`|16|ok
31 may|110k|truephile|baseline|`./src/run_model_basic.py -d /data/sef/bert_cls-110k-p.embd -f 2 -nn truephile -mn bert_cls > runs/basic_truephile.log`|13|ok
31 may|110k|nimonic|sub feeder|`./src/run_model_basic.py -d "/data/sef/bert_cls_(subl0.75)-110k-p.embd" -f 1 -nn nimonic_l75 -mn bert_cls > "runs/basic_nimonic_(subl0.75).log"`|12|killed, ok (stopped)
31 may|110k|nimonic|sub feeder|`./src/run_model_basic.py -d "/data/sef/bert_cls_(subr0.25)-110k-p.embd" -f 1 -nn nimonic_r25 -mn bert_cls > "runs/basic_nimonic_(subr0.25).log"`|12|killed, ok (stopped)
31 may|110k|nimonic|sub feeder|`./src/run_model_basic.py -d "/data/sef/bert_cls_(subr0.5)-110k-p.embd"  -f 1 -nn nimonic_r5  -mn bert_cls > "runs/basic_nimonic_(subr0.5).log"` |11|killed, ok (stopped)
31 may|110k|nimonic|sub feeder|`./src/run_model_basic.py -d "/data/sef/bert_cls_(subr0.75)-110k-p.embd" -f 1 -nn nimonic_r75 -mn bert_cls > "runs/basic_nimonic_(subr0.75).log"`|10|killed, ok (stopped)
1 jun|46+10k|clover_46k|limited data|`./src/run_model_basic.py -d "/data/sef/bert_cls-110k-p.embd" -f 1 -nn clover_46k -mn bert_cls -tn 46000 > runs/basic_clover_46k.log`|8|ok (stopped)
2 jun|5+10k|kora_5k|limited data|`./src/run_model_basic.py -d "/data/sef/bert_cls-110k-p.embd" -f 6 -nn kora_5k -mn bert_cls -tn 5000 > runs/basic_kora_5k.log`|13|ok
2 jun|8+10k|kora_8k|limited data|`./src/run_model_basic.py -d "/data/sef/bert_cls-110k-p.embd" -f 6 -nn kora_8k -mn bert_cls -tn 8000 > runs/basic_kora_8k.log`|12|ok
2 jun|13+10k|kora_13k|limited data|`./src/run_model_basic.py -d "/data/sef/bert_cls-110k-p.embd" -f 6 -nn kora_13k -mn bert_cls -tn 13000 > runs/basic_kora_13k.log`|11|ok
2 jun|20+10k|kora_20k|limited data|`./src/run_model_basic.py -d "/data/sef/bert_cls-110k-p.embd" -f 6 -nn kora_20k -mn bert_cls -tn 20000 > runs/basic_kora_20k.log`|10|ok (stopped)
2 jun|31+10k|kora_31k|limited data|`./src/run_model_basic.py -d "/data/sef/bert_cls-110k-p.embd" -f 6 -nn kora_31k -mn bert_cls -tn 31000 > runs/basic_kora_31k.log`|8|ok (stopped)
2 jun|46+10k|kora_46k|limited data|`./src/run_model_basic.py -d "/data/sef/bert_cls-110k-p.embd" -f 6 -nn kora_46k -mn bert_cls -tn 46000 > runs/basic_kora_46k.log`|16|ok (stopped)
2 jun|5+10k|tesera_5k|limited data|`./src/run_model_basic.py -d "/data/sef/bert_cls-110k-p.embd" -f 5 -nn tesera_5k -mn bert_cls -tn 5000 > runs/basic_tesera_5k.log`|13|ok
2 jun|5+10k|transom_5k|limited data|`./src/run_model_basic.py -d "/data/sef/bert_cls-110k-p.embd" -f 5 -nn transom_5k -mn bert_cls -tn 5000 > runs/basic_transom_5k.log`|13|ok
31 may|110k|nimonic|sub feeder|`./src/run_model_basic.py -d "/data/sef/bert_cls_(subl0.5)-110k-p.embd"  -f 1 -nn nimonic_l5  -mn bert_cls > "runs/basic_nimonic_(subl0.5).log"` |13|killed, ok (stopped)
31 may|110k|nimonic|sub feeder|`./src/run_model_basic.py -d "/data/sef/bert_cls_(subl0.25)-110k-p.embd" -f 1 -nn nimonic_l25 -mn bert_cls > "runs/basic_nimonic_(subl0.25).log"`|13|killed, ok (stopped)
1 jun|31+10k|clover_31k|limited data|`./src/run_model_basic.py -d "/data/sef/bert_cls-110k-p.embd" -f 1 -nn clover_31k -mn bert_cls -tn 31000 > runs/basic_clover_31k.log`|8|ok (stopped)
1 jun|20+10k|clover_20k|limited data|`./src/run_model_basic.py -d "/data/sef/bert_cls-110k-p.embd" -f 1 -nn clover_20k -mn bert_cls -tn 20000 > runs/basic_clover_20k.log`|10|ok (stopped)
1 jun|13+10k|clover_13k|limited data|`./src/run_model_basic.py -d "/data/sef/bert_cls-110k-p.embd" -f 1 -nn clover_13k -mn bert_cls -tn 13000 > runs/basic_clover_13k.log`|11|ok
1 jun|8+10k|clover_8k|limited data|`./src/run_model_basic.py -d "/data/sef/bert_cls-110k-p.embd" -f 1 -nn clover_8k -mn bert_cls -tn 8000 > runs/basic_clover_8k.log`|12|ok
1 jun|5+10k|clover_5k|limited data|`./src/run_model_basic.py -d "/data/sef/bert_cls-110k-p.embd" -f 1 -nn clover_5k -mn bert_cls -tn 5000 > runs/basic_clover_5k.log`|13|ok
1, 20 may|100k|sadmate_1|dynamic|`./src/run_model_dynamic.py -d /data/sef/bert_cls-110k-p.embd -f 1 --ps 0to1 -nn sadmate_1 -mn bert_cls -v 8192 > runs/dynamic_sadmate_1.log`|16, 15, 14, 12|ok, ok, stopped, ok
1, 20 may|100k|skewedapple_1|dynamic|`./src/run_model_dynamic.py -d /data/sef/bert_cls-110k-p.embd -f 1 --ps 1to0 -nn skewedapple_1 -mn bert_cls -v 8192 > runs/dynamic_skewedapple_1.log`|16, 15, 14, 12|ok, ok, stopped, ok
1, 13, 20 may|100k+10k|hector|cross|`./src/run_model_basic.py -d /data/sef/bert_cls-110k-p.embd -d2 /data/sef/news_bert_cls-10k-p.embd -f 1 -nn hector_1 -mn bert_cls > runs/cross_hector_1.log`|12,16|stopped, ok
20 may|100k|truedog|baseline (100k+10k)|`./src/run_model_basic.py -d /data/sef/bert_cls-110k-p.embd -f 0 -nn truedog -mn bert_cls > runs/basic_truedog.log`|8|ok
20 may|100k|truetit|baseline (100k+10k)|`./src/run_model_basic.py -d /data/sef/bert_cls-110k-p.embd -f 1 -nn truetit -mn bert_cls > runs/basic_truetit.log`|8|ok
13, 20 may|100k|hector|cross|`./src/run_model_basic.py -d /data/sef/bert_cls-110k-p.embd -d2 /data/sef/news_bert_cls-10k-p.embd -f 0 -nn hector_0 -mn bert_cls > runs/cross_hector_0.log`|12|stopped, running (may fail)
13, 19 may|100k+10k|iterum|cross|`./src/run_model_basic.py -d /data/sef/bert_cls-110k.embd -d2 /data/sef/books_bert_cls-10k.embd -f 0 -nn iterum_0 -mn bert_cls > runs/cross_iterum_0.log`|15,12,16|fail, fail, stopped, ok
20 may|100k+10k|iterum|cross|`./src/run_model_basic.py -d /data/sef/bert_cls-110k-p.embd -d2 /data/sef/books_bert_cls-10k-p.embd -f 1 -nn iterum_1 -mn bert_cls > runs/cross_iterum_1.log`|16|ok
24 may|110k+sub||embd sim|`./src/figures/embd_sim.py -ck > "runs/sim_embd.log"`|13|ok
20 may|110k|nimonic|embd subr|`./src/misc/embd.py -n 110000 -p --feeder subr --feeder-k 0.5 > "runs/embd_nimonic_(subr0.5).log"`|12|ok
20 may|110k|nimonic|embd subr|`./src/misc/embd.py -n 110000 -p --feeder subr --feeder-k 0.75 > "runs/embd_nimonic_(subr0.75).log"`|11|ok
20 may|110k|nimonic|embd subr|`./src/misc/embd.py -n 110000 -p --feeder subr --feeder-k 0.25 > "runs/embd_nimonic_(subr0.25).log"`|11|ok
20 may|110k|nimonic|embd subl|`./src/misc/embd.py -n 110000 -p --feeder subl --feeder-k 0.5 > "runs/embd_nimonic_(subl0.5).log"`|11|ok
20 may|110k|nimonic|embd subl|`./src/misc/embd.py -n 110000 -p --feeder subl --feeder-k 0.75 > "runs/embd_nimonic_(subl0.75).log"`|10|ok
20 may|110k|nimonic|embd subl|`./src/misc/embd.py -n 110000 -p --feeder subl --feeder-k 0.25 > "runs/embd_nimonic_(subl0.25).log"`|10|ok
20 may|10k||embd|`./src/misc/embd.py -n 10000 -m bert --type-out cls -d news --bpe-encoder /data/sef/s110k-v8192.enc_pkl -p > runs/embd_10k_news_bert_cls_p.log`|16|ok
19 may|110k||embd|`./src/misc/embd.py -n 110000 -m bert --type-out cls -p > runs/embd_110k_bert_cls_p.log`|16|ok
19 may|10k||embd|`./src/misc/embd.py -n 10000 -m bert --type-out cls -d books --bpe-encoder /data/sef/s110k-v8192.enc_pkl -p > runs/embd_10k_books_bert_cls_p.log`|16|ok
19 may|10k||embd|`./src/misc/embd.py -n 10000 -m bert --type-out cls -d books --bpe-encoder /data/sef/s110k-v8192.enc_pkl > runs/embd_10k_books_bert_cls.log`|16|ok
19 may|110k||embd|`./src/misc/embd.py -n 110000 -m bert --type-out cls > runs/embd_110k_bert_cls.log`|16|ok
19 may|10k+1k|viparous|cross|`./src/run_model_basic.py -d /data/sef/bert_cls-10k-p.embd -d2 /data/sef/bert_cls-10k-p.embd -f 0 -nn viparous -mn bert_cls -v 8192`|16|ok
19 may|1k|viparous|embd|`./src/misc/embd.py -n 1000 -m bert --dataset books --type-out cls`|16|ok
19 may|10k+1k|jeremiad|cross|`./src/run_model_basic.py -d /data/sef/bert_cls-10k.embd -d2 /data/sef/bert_cls-1k.embd -f 0 -nn jeremiad_cross -,n bert_cls`|16|ok
19 may|10k|jeremiad|basic|`./src/run_model_basic.py -d /data/sef/bert_cls-10k.embd -f 0 -nn jeremiad -mn bert_cls -v 8192`|16|ok
19 may|10k|jeremiad|embd bert cls, cross, prefix|`./src/misc/embd.py -n 2000 -m bert --type-out cls -p`|16|ok, ok
16 may|100k|geoponic|cross|`./src/run_model_basic.py -d /data/sef/bert_cls-100k-p.embd -d2 /data/sef/bert_cls-1k-p.embd -f 1 -nn geoponic -mn bert_cls -v 8192`|16|stopped (fail)
21, 27, 29 apr, 13 may|1k||{books,news}, embd bert cls|`./src/misc/embd.py -n 1000 -m bert --type-out cls --dataset books -p --bpe-encoder /data/sef/s100k-v8192.enc_pkl`|13, wx|fail,fail,fail,ok
1 may|100k|eurythmics|vectorizer|`./src/run_model_basic.py -d /data/sef/tfidf-100k-p.embd -f 1 -nn eurythmics -mn tfidf -v 8192`|15|ok
1 may|100k|septenary|vectorizer|`./src/run_model_basic.py -d /data/sef/count-100k-p.embd -f 1 -nn septenary -mn count -v 8192`|15|ok
1 may|100k|sadmate_5|dynamic|`./src/run_model_dynamic.py -d /data/sef/bert_cls-100k-p.embd -f 5 --ps 0to1 -nn sadmate_5 -mn bert_cls -v 8192`|16|bad
1 may|100k|skewedapple_5|dynamic|`./src/run_model_dynamic.py -d /data/sef/bert_cls-100k-p.embd -f 5 --ps 1to0 -nn skewedapple_5 -mn bert_cls -v 8192`|16|bad
1 may|100k|wankle|baseline|`./src/run_model_basic.py -d /data/sef/bert_avg-100k-p.embd -f 1 -nn wankle -mn bert_avg -v 8192`|15|ok
1 may|100k|provand|baseline|`./src/run_model_basic.py -d /data/sef/sbert_avg-100k-p.embd -f 1 -nn provand -mn sbert_avg -v 8192`|15|ok
1 may|100k|raster|baseline|`./src/run_model_basic.py -d /data/sef/sbert_cls-100k-p.embd -f 1 -nn raster -mn sbert_cls -v 8192`|15|ok
28, 29 apr|100k|petit|baseline|`./src/run_model_basic.py -d /data/sef/bert_cls-100k-p.embd -f 1 -nn petit -mn bert_cls -v 8192`|15|ok
28, 29 apr|100k|bluedog|baseline|`./src/run_model_basic.py -d /data/sef/bert_cls-100k-p.embd -f 0 -nn bluedog -mn bert_cls -v 8192`|15|ok
28, 29 apr|100k|thamin||`./src/run_model_basic.py -d /data/sef/bert_cls-100k-p.embd -f 6 -nn thamin -mn bert_cls -v 8192`|15|ok
28, 29 apr|100k|vacuum||`./src/run_model_basic.py -d /data/sef/bert_cls-100k-p.embd -f 3 -nn vacuum -mn bert_cls -v 8192`|15|ok
29 apr|100k|technophile||`./src/run_model_basic.py -d /data/sef/bert_cls-100k-p.embd -f 2 -nn technophile -mn bert_cls -v 8192`|13|ok
29 apr|100k|outjet||`./src/run_model_basic.py -d /data/sef/bert_cls-100k-p.embd -f 4 -nn outjet -mn bert_cls -v 8192`|13|ok
29 apr|100k|guffle||`./src/run_model_basic.py -d /data/sef/bert_cls-100k-p.embd -f 5 -nn guffle -mn bert_cls -v 8192`|13|ok
27,28 apr|100k||embd sbert {cls,avg}, prefix|`./src/misc/embd.py -n 100000 -m sbert --type-out cls -p`|15|ok, ok
27,28 apr|100k||embd bert {cls,avg}, prefix|`./src/misc/embd.py -n 100000 -m bert --type-out cls -p`|15|ok, ok
27,28 apr|100k||embd count, tfidf||15|ok, ok
27,28 apr|100k||embd sbert {cls,avg}|`./src/misc/embd.py -n 100000 -m sbert --type-out cls`|15|ok, ok
27,28 apr|100k||embd bert {cls,avg}|`./src/misc/embd.py -n 100000 -m bert --type-out cls`|15|ok, ok

## Finished (old)

(re)start|action|command|machine|status
-|-|-|-|-
21, 27 apr|1m||embd bert cls||16|fail,not saved 
27 apr|100k, embd sbert cls||15|ok
27 apr|100k, embd bert cls||15|ok
21 apr|1m, embd bert cls prefix||16|fail,cancel 
15 apr|5k, *septenary*, prefix, count, `-f 1`||16|ok
15 apr|5k, *eurythmics*, prefix, tfidf, `-f 1`||16|ok
15 apr|5k, *jade*, prefix, bert-cls, `-f 1`||16|ok
15 apr|5k, *guidam*, baseline `-f 0`||16|ok
15 apr|5k, embd bert cls ||16|ok
8 apr|5k, *fustigate*, prefix, bert-cls, train: shuffle 1 dev: shuffle 1, `-f 1`||16|bad code, ok
8 apr|5k, *rubinetto*, prefix, bert-cls, train: shuffle 0 dev: shuffle 1, `-f 1`||15,16|bad code, ok
8 apr|5k, *jersey*, prefix, bert-cls, train: shuffle 0 dev: shuffle 2, `-f 1`||15|bad code, ok
8 apr|5k, *sapid*, prefix, bert-cls, train: shuffle 2 dev: shuffle 2, `-f 1`||15|bad code, ok
8 apr|5k, *yeowoman*, cheat, bert-cls, basic fusion, `-f 1`||15|ok
7 apr|5k, outjet, prefix, bert-cls, `-f 4`||15|ok
7 apr|5k, guffle, prefix, bert-cls, `-f 5`||15|ok
7 apr|5k, thamin, prefix, bert-cls, `-f 6`||15|ok
25 mar, 1 apr|5k, wankle, cheat, bert-avg, `-f 1`||15|ok, ok
25 mar, 1 apr|5k, provand, cheat, sbert-avg, `-f 1`||15|ok, ok
25 mar, 1 apr|5k, raster, cheat, sbert-cls, `-f 1`||15|ok, ok
25 mar, 1 apr|5k, ferous, cheat, bert-cls, `-f 1`||15|ok, ok
31 mar|5k, deltiology, tied embd layers, bert-cls, `-f 0`||15|ok
31 mar|5k, bombaster, separate embd layers, bert-cls, `-f 0`||15|ok
31 mar|5k, petit, baseline, bert-cls, `-f 1`||15|ok
31 mar|5k, bluedog, baseline, `-f 0`||15|ok
22 mar, 31 mar|5k sadmate, prefix, `-f 1 ps=1.0,0.75,0.5,0.25,0.0`||15|bad code, repeat, ok, ok
22 mar, 31 mar|5k skewedapple, prefix, `-f 1 ps=0.0,0.25,0.5,0.75,1.0`||14|bad code, ok
24 mar|embd 5k bert-avg, sbert-avg, sbert-cls, sbert-cls-p||14|ok
24 mar|100k keystone, prefix, `-f 1`||15|ok
24 mar|100k jalouse, cheat, `-f 1`||15|ok
24 mar|100k fatidical, prefix, `-f 0`||15|ok
22 mar|embd 100k all||15|ok
22 mar|100k sent redbeets (??)||16|running
22 mar|5k technophile, prefix, `-f 2 --hidden-size 768`||16|bad code, ok
22 mar|5k vacuum, prefix, `-f 3 --hidden-size 768`||16|bad code, ok
22 mar|5k bardel, prefix, `-f 1 --hidden-size 768`||16|ok
22 mar|5k grum, prefix, `-f 0 --hidden-size 768`||16|ok
22 mar|5k hardcarrot, prefix, `-f 1 ps=0.9,0.8,0.7,0.6,0.5`||16|ok
22 mar|5k wettissue, prefix, `-f 1 ps=0.6,0.7,0.8,0.9,1.0`||16|bad code, ok
22 mar|1k sent||16|ok
10-20 mar|various embd + fusion||16|ok
10 mar|1mil sentence embd (nohup.out)||16|ok
||||