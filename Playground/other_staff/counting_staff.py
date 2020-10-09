def _test(A, B):
    return (5 * ((A + B) / 4 + B + A) / 4) - (A + B) / 4


if __name__ == "__main__":
    print(_test(1, 1))
    print(_test(100, 100))
    print(_test(500, 500))

    print(_test(5, 500))
    print(_test(500, 5))

    print(_test(300, 300))

    print(_test(1000, 10000))
