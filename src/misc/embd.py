#!/usr/bin/env python3

from datasets import load_dataset
import torch
import numpy as np
from transformers import BertTokenizer, BertModel
from transformers import AutoTokenizer, AutoModel
from utils import get_device, save_pickle
from nltk import sent_tokenize
from tqdm import tqdm
from argparse import ArgumentParser
from bpe import Encoder

DEVICE = get_device()


def mean_pooling(model_output, attention_mask, layer_i=0):
    # Mean Pooling - Take attention mask into account for correct averaging
    # first element of model_output contains all token embedding
    token_embeddings = model_output[layer_i]
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(
        token_embeddings.size()
    ).float()
    sum_embeddings = torch.sum(token_embeddings * input_mask_expanded, 1)
    sum_mask = torch.clamp(input_mask_expanded.sum(1), min=1e-9)
    return (sum_embeddings / sum_mask).reshape(-1)


class BertWrap():
    def __init__(self):
        self.tokenizer = BertTokenizer.from_pretrained(
            "bert-base-cased"
        )
        self.model = BertModel.from_pretrained(
            "bert-base-cased", return_dict=True, output_hidden_states=True
        )
        self.model.train(False)
        self.model.to(DEVICE)

    def embd(self, sentence, type_out):
        encoded_input = self.tokenizer(
            sentence, padding=True,
            truncation=True, max_length=128,
            return_tensors='pt'
        )
        encoded_input = encoded_input.to(DEVICE)
        with torch.no_grad():
            output = self.model(**encoded_input)
        if type_out == "cls":
            return output[0][0, 0].cpu().numpy()
        elif type_out in {"pooler", "pool"}:
            return output["pooler_output"][0].cpu().numpy()
        elif type_out in {"tokens", "avg"}:
            sentence_embedding = mean_pooling(
                output, encoded_input['attention_mask'])
            return sentence_embedding.cpu().numpy()
        else:
            raise Exception("Unknown type out")


class SentenceBertWrap():
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(
            "sentence-transformers/bert-base-nli-cls-token")
        self.model = AutoModel.from_pretrained(
            "sentence-transformers/bert-base-nli-cls-token")
        self.model.train(False)
        self.model.to(DEVICE)

    def embd(self, sentence, type_out):
        encoded_input = self.tokenizer(
            sentence, padding=True, truncation=True, max_length=128, return_tensors='pt')
        encoded_input = encoded_input.to(DEVICE)
        with torch.no_grad():
            output = self.model(**encoded_input)
        if type_out == "cls":
            return output[0][0, 0].cpu().numpy()
        elif type_out in {"pooler", "pool"}:
            return output["pooler_output"][0].cpu().numpy()
        elif type_out in {"tokens", "avg"}:
            sentence_embedding = mean_pooling(
                output, encoded_input['attention_mask']
            )
            return sentence_embedding.cpu().numpy()
        else:
            raise Exception("Unknown type out")

if __name__ == "__main__":
    args = ArgumentParser()
    args.add_argument("-n", help="Number of sentences", type=int, default=1000)
    args.add_argument("-m", "--model", default="bert")
    args.add_argument("--type-out", default="cls")
    args.add_argument(
        "-p", "--prefix", help="Embed prefixes",
        action="store_true"
    )
    args.add_argument("-v", "--vocab-size", type=int, default=1024)
    args = args.parse_args()

    dataset = load_dataset("wikitext", "wikitext-103-v1")

    sentences = []
    encoder = Encoder(vocab_size=args.vocab_size)
    print(len(dataset["train"]), "total paragraphs")
    # this assumes that every line has at least one sentence
    for sent in tqdm(dataset["train"][:args.n]["text"]):
        sentences += sent_tokenize(sent)

    sentences = sentences[:args.n]
    sentences = ["BOS " + x + " EOS" for x in sentences]
    encoder.fit(sentences)
    sentences_bpe = list(encoder.transform(sentences))
    sentences = [(x, y[:512]) for x, y in zip(sentences, sentences_bpe)]
    print(len(sentences), "total sentences")

    if args.model == "bert":
        model = BertWrap()
    elif args.model in {"sbert", "sentencebert"}:
        model = SentenceBertWrap()
    sentences_embd = []

    for sent, sent_bpe in tqdm(sentences, mininterval=60):
        if not args.prefix:
            output = np.tile(
                model.embd(sent, type_out=args.type_out),
                (len(sent_bpe) - 1, 1)
            )
        else:
            print(list(encoder.inverse_transform([sent_bpe[:5]]))[0])
            output = [
                model.embd(
                    list(encoder.inverse_transform([sent_bpe[:i]]))[0],
                    type_out="cls"
                )
                for i in range(1, len(sent_bpe))
            ]
            print(len(output), output[0].shape)
        # text, BPE (ids), embedding
        sentences_embd.append((sent, sent_bpe, output))

    save_pickle(
        f"/data/sef/{args.model}_{args.type_out}-{args.n//1000}k{'-p' if args.prefix else ''}.embd",
        sentences_embd
    )

    save_pickle(
        f"/data/sef/s{args.n//1000}k-v{args.vocab_size}.enc_pkl",
        encoder
    )
