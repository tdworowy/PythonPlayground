if __name__ == "__main__":
    f = lambda x, y, z: print(x + y + z)
    f(1, 2, 3)
    f = lambda x, y, z: x + y + z
    print(f(1, 2, 3))

    L = [(lambda x: x**2), (lambda x: x**3), (lambda x: x**4)]

    for f in L:
        print(f(2))

    lower = lambda x, y: x if x < y else y
    print(lower("bb", "aa"))

    def action(x):
        return lambda y: x + y

    act = action(99)
    print(act)
    print(act(2))
    print(act(4))

    action = lambda x: (lambda y: x + y)
    act = action(99)
    print(act)
    print(act(2))
    print(act(4))
