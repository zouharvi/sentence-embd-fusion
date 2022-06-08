def get_feeder(name):
    if name in {None, "identity"}:
        return process_identity
    elif name in {"subl"}:
        return process_subl
    elif name in {"subr"}:
        return process_subr
    elif name in {"lrcontext"}:
        return process_lrcontext
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


def process_lrcontext(sentences, sentences_bpe, encoder, args):
    data = [
        (x, y) for x, y in zip(sentences, sentences_bpe)
        if len(y) <= 256
    ][:args.n]

    mask_token = list(encoder.transform(["[MASK]"]))[0]

    def remask(i, sent_bpe):
        # inject [MASK]
        tmp_sent = sent_bpe[:i] + mask_token + sent_bpe[i + 1:]
        sent = list(encoder.inverse_transform([tmp_sent]))[0]
        # hotfix segmentation
        # it's still going to be incorrectly segmented but the information flow should remain coherent
        sent = sent.replace("[ mask", "[MASK").replace("mask ]", "MASK]").replace("MASK ]", "MASK]")
        return sent

    print(len(data), "total sentences used")
    for sent, sent_bpe in data:
        yield (
            sent, sent_bpe,
            [
                remask(i, sent_bpe)
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
