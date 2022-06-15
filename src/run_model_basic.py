#!/usr/bin/env python3

from argparse import ArgumentParser
from misc.utils import read_pickle
import torch
import torch.nn.functional as F
import numpy as np
from model_basic import LSTMModel

torch.set_num_threads(10)

if __name__ == "__main__":
    args = ArgumentParser()
    args.add_argument("-d", "--data", default="/data/sef/missing.embd")
    args.add_argument("-d2", "--data-dev", default=None)
    args.add_argument("-f", "--fusion", type=int, default=0)
    args.add_argument("-nn", "--nick-name", default="")
    args.add_argument("-mn", "--model-name", default="bert")
    args.add_argument("-v", "--vocab-size", type=int, default=8192)
    args.add_argument("-e", "--epochs", type=int, default=100)
    args.add_argument("-tn", "--train-n", type=int, default=100000)
    args.add_argument("--encoder", default=None)
    args.add_argument("--ns-file", default=None)
    args.add_argument("--ns-file-out", default=None)
    args.add_argument("--hidden-size", type=int, default=768)
    args = args.parse_args()

    def encode_text(text):
        return (F.one_hot(text, num_classes=args.vocab_size)).float()

    if args.data_dev is not None:
        data_train = read_pickle(args.data)
        data_train = data_train[:args.train_n]
        data_dev = read_pickle(args.data_dev)
        data_dev = data_dev
    else:
        data = read_pickle(args.data)
        data_train = data[:args.train_n]
        data_dev = data[-10000:]

    print(f"Using {len(data_train)} for training")
    print(f"Using {len(data_dev)} for dev")

    data_dev = [
        (x[0], torch.LongTensor(np.array(x[1])), torch.FloatTensor(np.array(x[2])))
        for x in data_dev
    ]

    data_train = [
        (x[0], torch.LongTensor(np.array(x[1])), torch.FloatTensor(np.array(x[2])))
        for x in data_train
    ]

    if args.encoder is not None:
        encoder = read_pickle(args.encoder)
    else:
        encoder = None
    
    # natural stories special path
    if args.ns_file is not None:
        error_sents = set()
        data_ns_raw = read_pickle(args.ns_file)
        data_ns = []
        for sent_i, (sent, sent_ns) in enumerate(list(zip(data_dev, data_ns_raw))):
            sent_txt = sent[0]
            # remove BOS & EOS
            sent_bpe = encoder.tokenize(sent_txt)[1:-1]
            sent_tok = [t.lower() for t in sent_ns[0]]
            sent_alignment = []
            ptr_i = 0
            sent_txt = sent_txt.lower()
            error = False

            try:
                # perform alignment
                for i, word_bpe in enumerate(sent_bpe):
                    if word_bpe == "__sow" and len(sent_tok[ptr_i]) == 0:
                        ptr_i += 1
                    if word_bpe == "__sow" and len(sent_tok[ptr_i]) != 0:
                        # stay on the same word
                        pass
                    elif word_bpe == "__eow":
                        # stay on the same word
                        pass
                    elif word_bpe == "__unk":
                        # stay on the same word
                        pass
                    elif sent_tok[ptr_i].startswith(word_bpe):
                        # still in current word
                        sent_tok[ptr_i] = sent_tok[ptr_i][len(word_bpe):]
                    elif sent_tok[ptr_i+1].startswith(word_bpe):
                        # moving to the next word
                        sent_tok[ptr_i+1] = sent_tok[ptr_i+1][len(word_bpe):]
                        ptr_i += 1
                    else:
                        error = True
                        # print("Unable to match BPE", word_bpe, sent_tok[ptr_i], sent_tok[ptr_i+1])
                    
                    sent_alignment.append(ptr_i)
            except Exception as e:
                error = True

            if error:
                error_sents.add(sent_i)
            # txt, reading times, alignment
            data_ns.append((sent_ns[0], sent_ns[1], sent_alignment))

        # remove unaligned sentences
        data_dev = [x for i, x in enumerate(data_dev) if i not in error_sents]
        data_ns = [x for i, x in enumerate(data_ns) if i not in error_sents]
        print(len(error_sents), "sentences could not be aligned (skipping)")

    model = LSTMModel(
        args.vocab_size, fusion=args.fusion,
        hidden_size=args.hidden_size,
        encoder=encoder,
    )
    model.train_loop(
        data_train, data_dev,
        encode_text,
        prefix=f"{args.model_name}-{args.nick_name}",
        epochs=args.epochs,
        data_ns=data_ns,
    )
