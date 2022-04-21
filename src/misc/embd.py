#!/usr/bin/env python3

from datasets import load_dataset
import numpy as np
from utils import save_pickle, read_pickle
from nltk import sent_tokenize
from tqdm import tqdm
from argparse import ArgumentParser
from bpe import Encoder
from embd_models import BertWrap, SentenceBertWrap, CountVectorizerWrap, TfIdfVectorizerWrap

def get_dataset_data(dataset, args):
    if dataset == "wikitext":
        dataset = load_dataset("wikitext", "wikitext-103-v1")
    elif dataset in {"bookcorpus", "books"}:
        dataset = load_dataset("bookcorpus")
    elif dataset in {"cc_news", "news"}:
        dataset = load_dataset("cc_news")

    print(len(dataset["train"]), "total paragraphs")
    sentences = []
    # this assumes that every line has at least one sentence
    for sent in tqdm(dataset["train"][:args.n]["text"]):
        sentences += sent_tokenize(sent)
    return sentences

if __name__ == "__main__":
    args = ArgumentParser()
    args.add_argument("-n", help="Number of sentences", type=int, default=1000)
    args.add_argument("--bpe-encoder", default=None)
    args.add_argument("--dataset", default="wikitext")
    args.add_argument("-m", "--model", default="bert")
    args.add_argument("--type-out", default="cls")
    args.add_argument(
        "-p", "--prefix", help="Embed prefixes",
        action="store_true"
    )
    args.add_argument("-v", "--vocab-size", type=int, default=8192)
    args = args.parse_args()

    if args.bpe_encoder is not None:
        print("Loading BPE encoder")
        encoder = read_pickle(args.bpe_encoder)
    else:
        print("Creating a new BPE encoder")
        encoder = Encoder(vocab_size=args.vocab_size)

    sentences = get_dataset_data(args.dataset, args)
    print(len(sentences), "total sentences available (inaccurate)")
    sentences = sentences[:args.n]
    print(len(sentences), "total sentences used")

    if args.model in {"bert"}:
        model = BertWrap(type_out=args.type_out)
    elif args.model in {"sbert", "sentencebert"}:
        model = SentenceBertWrap(type_out=args.type_out)
    elif args.model in {"count"}:
        model = CountVectorizerWrap(text=sentences)
    elif args.model in {"tfidf"}:
        model = TfIdfVectorizerWrap(text=sentences)

    sentences = ["BOS " + x + " EOS" for x in sentences]
    print(f"{np.average([len(x.split()) for x in sentences]):.1f} avg words in a sentence")

    if args.model in {"bert", "sbert", "sentencebert"}:
        name_str = f"{args.model}_{args.type_out}"
    else:
        name_str = args.model

    if args.n >= 1000000:
        count_str = f"{args.n//1000000:.0f}m"
    elif args.n >= 1000:
        count_str = f"{args.n//1000:.0f}k"
    else:
        count_str = args.n


    if args.bpe_encoder is None:
        encoder.fit(sentences)

        save_pickle(
            f"/data/sef/s{count_str}-v{args.vocab_size}.enc_pkl",
            encoder
        )

    exit()

    sentences_bpe = list(encoder.transform(sentences))
    print(f"{np.average([len(x) for x in sentences_bpe]):.1f} avg subwords in a sentence")
    sentences = [(x, y[:512]) for x, y in zip(sentences, sentences_bpe)]

    sentences_embd = []

    for sent, sent_bpe in tqdm(sentences, miniters=1000):
        if not args.prefix:
            output = np.tile(
                model.embd(sent),
                (len(sent_bpe) - 1, 1)
            )
        else:
            output = [
                model.embd(
                    list(encoder.inverse_transform([sent_bpe[:i]]))[0],
                )
                for i in range(1, len(sent_bpe))
            ]
        # text, BPE (ids), embedding
        sentences_embd.append((sent, sent_bpe, output))

    save_pickle(
        f"/data/sef/{name_str}-{count_str}{'-p' if args.prefix else ''}.embd",
        sentences_embd
    )
