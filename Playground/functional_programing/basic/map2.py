def inc(x): return x + 10


if __name__ == "__main__":
    counters = [1, 2, 3, 4, 5, 6, 7, 8]
    map1 = map(inc, counters)
    mapL = list(map1)
    print(mapL)

    map2 = map((lambda x: x + 3), counters)

    mapL = list(map2)
    print(mapL)

    print(pow(3, 4))

    map3 = map(pow, [1, 2, 3], [1, 2, 3])

    mapL = list(map3)
    print(mapL)
