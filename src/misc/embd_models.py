#!/usr/bin/env python3

import torch
import numpy as np
from transformers import BertTokenizer, BertModel
from transformers import AutoTokenizer, AutoModel
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from utils import get_device
from tqdm import tqdm

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
    def __init__(self, type_out="cls"):
        self.type_out = type_out
        self.tokenizer = BertTokenizer.from_pretrained(
            "bert-base-cased"
        )
        self.model = BertModel.from_pretrained(
            "bert-base-cased", return_dict=True, output_hidden_states=True
        )
        self.model.train(False)
        self.model.to(DEVICE)

    def embd(self, sentence):
        encoded_input = self.tokenizer(
            sentence, padding=True,
            truncation=True, max_length=512,
            return_tensors='pt'
        )
        encoded_input = encoded_input.to(DEVICE)
        with torch.no_grad():
            output = self.model(**encoded_input)
        if self.type_out == "cls":
            return output[0][0, 0].cpu().numpy()
        elif self.type_out in {"pooler", "pool"}:
            return output["pooler_output"][0].cpu().numpy()
        elif self.type_out in {"tokens", "avg"}:
            sentence_embedding = mean_pooling(
                output, encoded_input['attention_mask'])
            return sentence_embedding.cpu().numpy()
        else:
            raise Exception("Unknown type out")


class SentenceBertWrap():
    def __init__(self, type_out="cls"):
        self.type_out = type_out
        self.tokenizer = AutoTokenizer.from_pretrained(
            "sentence-transformers/bert-base-nli-cls-token")
        self.model = AutoModel.from_pretrained(
            "sentence-transformers/bert-base-nli-cls-token")
        self.model.train(False)
        self.model.to(DEVICE)

    def embd(self, sentence):
        encoded_input = self.tokenizer(
            sentence, padding=True,
            truncation=True, max_length=512,
            return_tensors='pt'
        )
        encoded_input = encoded_input.to(DEVICE)
        with torch.no_grad():
            output = self.model(**encoded_input)
        if self.type_out == "cls":
            return output[0][0, 0].cpu().numpy()
        elif self.type_out in {"pooler", "pool"}:
            return output["pooler_output"][0].cpu().numpy()
        elif self.type_out in {"tokens", "avg"}:
            sentence_embedding = mean_pooling(
                output, encoded_input['attention_mask']
            )
            return sentence_embedding.cpu().numpy()
        else:
            raise Exception("Unknown type out")


class NoneWrap():
    def __init__(self):
        pass

    def embd(self, sentence):
        return torch.zeros((768,)).numpy()


class CountVectorizerWrap():
    def __init__(self, text):
        self.model = CountVectorizer(max_features=768)
        self.model.fit(text)

    def embd(self, sentence):
        return self.model.transform([sentence]).toarray()[0].astype(np.float32)

class TfIdfVectorizerWrap():
    def __init__(self, text):
        self.model = TfidfVectorizer(max_features=768)
        self.model.fit(text)

    def embd(self, sentence):
        return self.model.transform([sentence]).toarray()[0].astype(np.float32)