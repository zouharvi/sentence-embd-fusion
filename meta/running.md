## Running/staged

(re)start|size|nickname|description|command|machine|status
-|-|-|-|-|-|-
|||||||
27,28 apr|100k||embd count, tfidf||15|ok, running
27,28 apr|100k||embd sbert {cls,avg}, prefix|`./src/misc/embd.py -n 100000 -m sbert --type-out cls -p`|15|ok, running
27,28 apr|100k||embd sbert {cls,avg}|`./src/misc/embd.py -n 100000 -m sbert --type-out cls`|15|ok, running
27,28 apr|100k||embd bert {cls,avg}, prefix|`./src/misc/embd.py -n 100000 -m bert --type-out cls -p`|15|ok, running
27,28 apr|100k||embd bert {cls,avg}|`./src/misc/embd.py -n 100000 -m bert --type-out cls`|15|ok, running
28 apr|100k|petit|baseline|`./src/run_model_basic.py -d /data/sef/bert_cls-100k-p.embd -f 1 -nn petit -mn bert_cls -v 8192`|15|halted
28 apr|100k|bluedog|baseline|`./src/run_model_basic.py -d /data/sef/bert_cls-100k-p.embd -f 0 -nn bluedog -mn bert_cls -v 8192`|15|halted
28 apr|100k|thamin||`./src/run_model_basic.py -d /data/sef/bert_cls-100k-p.embd -f 6 -nn thamin -mn bert_cls -v 8192`|15|halted
28 apr|100k|vacuum||`./src/run_model_basic.py -d /data/sef/bert_cls-100k-p.embd -f 3 -nn vacuum -mn bert_cls -v 8192`|15|halted

## Finished (old)

(re)start|action|command|machine|status
-|-|-|-|-
|||||
||||finished
21, 27 apr|1m||embd bert cls||16|fail,not saved 
21, 27 apr|1k, {books,news}, embd bert cls prefix||15|fail,ok
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