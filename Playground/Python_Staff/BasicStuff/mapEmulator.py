def my_map(func, *seqs):
    res = []
    for args in zip(*seqs):
        res.append(func(*args))
    return res


def my_map2(func, *seqs):
    return [func(*args) for args in zip(*seqs)]


def my_map3(func, *seqs):
    for args in zip(*seqs):
        yield (func(*args))


def my_map4(func, *seqs):
    return (func(*args) for args in zip(*seqs))

if __name__ == "__main__":


    print(my_map(abs, [2, 1, 0, 1, -2]))
    print(my_map(pow, [2, 1, 0, 1, 2], [2, 3, 0, 5, 2]))

    print(my_map2(abs, [2, 1, 0, 1, -2]))
    print(my_map2(pow, [2, 1, 0, 1, 2], [2, 3, 0, 5, 2]))

    print(list(my_map3(abs, [2, 1, 0, 1, -2])))
    print(list(my_map3(pow, [2, 1, 0, 1, 2], [2, 3, 0, 5, 2])))

    print(list(my_map4(abs, [2, 1, 0, 1, -2])))
    print(list(my_map4(pow, [2, 1, 0, 1, 2], [2, 3, 0, 5, 2])))
