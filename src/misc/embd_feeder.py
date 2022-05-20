def get_feeder(name):
    if name in {None, "identity"}:
        return process_identity
    elif name in {"subl"}:
        return process_subl
    elif name in {"subr"}:
        return process_subr
    raise Exception("Unknown feeder")


def process_identity(sentences, sentences_bpe, encoder, args):
    data = [
        (x, y) for x, y in zip(sentences, sentences_bpe)
        if len(y) <= 256
    ][:args.n]
    print(len(data), "total sentences used")
    for sent, sent_bpe in data:
        yield (
            sent, sent_bpe,
            [
                list(encoder.inverse_transform([sent_bpe[:i]]))[0]
                for i in range(1, len(sent_bpe))
            ]
        )


def process_subl(sentences, sentences_bpe, encoder, args):
    data = [
        (x, y) for x, y in zip(sentences, sentences_bpe)
        if len(y) <= 256
    ][:args.n]
    print(len(data), "total sentences used")
    for sent, sent_bpe in data:
        pos_k = int(args.feeder_k * len(sent_bpe))
        yield (
            sent, sent_bpe,
            [
                list(encoder.inverse_transform([sent_bpe[pos_k:i]]))[0]
                for i in range(1, len(sent_bpe))
            ]
        )


def process_subr(sentences, sentences_bpe, encoder, args):
    data = [
        (x, y) for x, y in zip(sentences, sentences_bpe)
        if len(y) <= 256
    ][:args.n]
    print(len(data), "total sentences used")
    for sent, sent_bpe in data:
        pos_k = int(args.feeder_k * len(sent_bpe))
        yield (
            sent, sent_bpe,
            [
                list(encoder.inverse_transform([
                    sent_bpe[:min(i, pos_k)]
                ]))[0]
                for i in range(1, len(sent_bpe))
            ]
        )
