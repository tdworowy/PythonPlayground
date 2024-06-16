def intersect(*args):
    res = []
    for x in args[0]:
        for other in args[1:]:
            if x not in other:
                break
        else:
            res.append(x)
    return res


def union(*args):
    res = []
    for seq in args:
        for x in seq:
            if not x in res:
                res.append(x)
    return res


if __name__ == "__main__":
    s1, s2, s3 = "Teodor", "Teofil", "Troll"

    print(intersect(s1, s2), union(s1, s2))
    print(intersect([1, 3, 2], [1, 4]))
    print(intersect(s1, s2, s3))
    print(union(s1, s2, s3))

    # can use sets operations
