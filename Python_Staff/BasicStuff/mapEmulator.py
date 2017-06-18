def myMap(func, *seqs):
    res = []
    for args in zip(*seqs):
        res.append(func(*args))
    return res


def myMap2(func, *seqs):
    return [func(*args) for args in zip(*seqs)]


def myMap3(func, *seqs):
    for args in zip(*seqs):
        yield (func(*args))


def myMap4(func, *seqs):
    return (func(*args) for args in zip(*seqs))


print(myMap(abs, [2, 1, 0, 1, -2]))
print(myMap(pow, [2, 1, 0, 1, 2], [2, 3, 0, 5, 2]))

print(myMap2(abs, [2, 1, 0, 1, -2]))
print(myMap2(pow, [2, 1, 0, 1, 2], [2, 3, 0, 5, 2]))

print(list(myMap3(abs, [2, 1, 0, 1, -2])))
print(list(myMap3(pow, [2, 1, 0, 1, 2], [2, 3, 0, 5, 2])))

print(list(myMap4(abs, [2, 1, 0, 1, -2])))
print(list(myMap4(pow, [2, 1, 0, 1, 2], [2, 3, 0, 5, 2])))
