from tqdm import tqdm

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
        (x, y)
        for x, y in zip(sentences, sentences_bpe)
        if len(y) <= 256
    ][:args.n]
    print(len(sentences), "total sentences used")
    for sent, sent_bpe in zip(sentences, sentences_bpe):
        yield (
            sent,
            [
                list(encoder.inverse_transform([sent_bpe[:i]]))[0]
                for i in range(1, len(sent_bpe))
            ]
        )


def process_subl(sentences, sentences_bpe, args):
    data = [
        (x, y) for x, y in zip(sentences, sentences_bpe)
        if len(y) <= 256 and len(y) >= 128
    ][:args.n]
    print(len(sentences), "total sentences used")
    for sent, sent_bpe in zip(sentences, sentences_bpe):
        yield (
            sent,
            [
                list(encoder.inverse_transform([sent_bpe[args.sub:i]]))[0]
                for i in range(128, len(sent_bpe))
            ]
        )


def process_subr(sentences, sentences_bpe, args):
    data = [
        (x, y) for x, y in zip(sentences, sentences_bpe)
        if len(y) <= 256 and len(y) >= 128
    ][:args.n]
    print(len(sentences), "total sentences used")
    for sent, sent_bpe in zip(sentences, sentences_bpe):
        yield (
            sent,
            [
                list(encoder.inverse_transform(
                    [sent_bpe[:min(i, args.sub)]]
                ))[0]
                for i in range(128, len(sent_bpe))
            ]
        )
