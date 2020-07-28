def my_sum(l):
    print(l)
    try:
        if not l:
            return 0
        else:
            return l[0] + my_sum(l[1:])
    except RecursionError  as re:
        print(re)
        return 0


def my_sum2(l):
    try:
        first, *rest = l
        print(l)
        return first if not rest else first + my_sum2(rest)
    except RecursionError  as re:
        print(re)
        return 0
    except MemoryError  as re:
        print(re)
        return 0


def sum_tree(l):
    tot = 0
    for x in l:
        if not isinstance(x, list):
            tot += x
        else:
            tot += sum_tree(x)
    print(tot)
    return tot


if __name__ == "__main__":

    l = list(range(1, 999999, 1))
    l2 = list(range(1, 99, 1))
    L = [1, [2, [3, [4, 5, 5], 6, 8], 2], 5]
    print(sum_tree(L))
