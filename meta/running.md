## TODO
- debug cross-domain
- add "empty feeder"
- cross-domain "self"
- joint vocab with out of domain 

## Running/staged

(re)start|size|nickname|description|command|machine|status
-|-|-|-|-|-|-
19 may|110k||embd|`./src/misc/embd.py -n 110000 -m bert --type-out cls > runs/embd_110k_bert_cls.log`|16|running
19 may|110k||embd|`./src/misc/embd.py -n 110000 -m bert --type-out cls -p > runs/embd_110k_bert_cls_p.log`|16|running
19 may|10k||embd|`./src/misc/embd.py -n 10000 -m bert --type-out cls -d books --bpe-encoder /data/sef/s110k-v8192.enc_pkl > runs/embd_10k_books_bert_cls.log`|16|running
1, 13 may|100k|hector|cross|`./src/run_model_basic.py -d /data/sef/bert_cls-100k-p.embd -d2 /data/sef/news_bert_cls-1k-p.embd -f 1 -nn hector_1 -mn bert_cls -v 8192`|12|stopped
13 may|100k|hector|cross|`./src/run_model_basic.py -d /data/sef/bert_cls-100k-p.embd -d2 /data/sef/news_bert_cls-1k-p.embd -f 0 -nn hector_0 -mn bert_cls -v 8192`|12|stopped
1, 13 may|100k|iterum|cross|`./src/run_model_basic.py -d /data/sef/bert_cls-100k-p.embd -d2 /data/sef/books_bert_cls-1k-p.embd -f 1 -nn iterum_1 -mn bert_cls -v 8192`|15, 12|stopped
1, 13 may|100k|iterum|cross|`./src/run_model_basic.py -d /data/sef/bert_cls-100k-p.embd -d2 /data/sef/books_bert_cls-1k-p.embd -f 0 -nn iterum_0 -mn bert_cls -v 8192`|15,12|fail, fail, stopped
1 may|100k|sadmate_1|dynamic|`./src/run_model_dynamic.py -d /data/sef/bert_cls-100k-p.embd -f 1 --ps 0to1 -nn sadmate_1 -mn bert_cls -v 8192`|16, 15, 14|ok, ok, stopped
1 may|100k|skewedapple_1|dynamic|`./src/run_model_dynamic.py -d /data/sef/bert_cls-100k-p.embd -f 1 --ps 1to0 -nn skewedapple_1 -mn bert_cls -v 8192`|16, 15, 14|ok, ok, stopped

## Finished
(re)start|size|nickname|description|command|machine|status
-|-|-|-|-|-|-
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