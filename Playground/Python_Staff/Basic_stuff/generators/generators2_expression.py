"""generator expression"""
if __name__ == "__main__":

    test = (x ** 2 for x in range(10))
    print(test)
    print(list(test))

    test = (x ** 2 for x in range(10))
    print(next(test))
    print(next(test))

    for num in (x ** 2 for x in range(10)):
        print('%s, %s' % (num, num / 2.0))

    G = (c * 4 for c in "SPAM")
    i1 = iter(G)
    i2 = iter(G)

    print(next(i1))  # for generators there is only one iterator per generator
    print(next(i1))
    print(next(i2))
