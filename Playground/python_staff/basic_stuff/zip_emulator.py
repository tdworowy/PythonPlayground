def myzip(*seqs):
    seqs = [list(S) for S in seqs]
    res = []
    while all(seqs):
        res.append(tuple(S.pop(0) for S in seqs))
    return res


def myzip2(*seqs):
    seqs = [list(S) for S in seqs]
    while all(seqs):
        yield (tuple(S.pop(0) for S in seqs))


def myzip3(*seqs):
    minlen = min(len(S) for S in seqs)
    return [tuple(S[i] for S in seqs) for i in range(minlen)]


def myzip4(*seqs):
    minlen = min(len(S) for S in seqs)
    return (tuple(S[i] for S in seqs) for i in range(minlen))


def myzip5(*args):
    iters = list(map(iter, args))
    while iters:
        res = [next(i) for i in iters]
        yield tuple(res)


if __name__ == "__main__":
    s1, s2 = "abc", "def"

    print(myzip(s1, s2))
    print(list(myzip2(s1, s2)))
    print(myzip3(s1, s2))
    print(list(myzip4(s1, s2)))

    print(list(myzip5(s1, s2)))
