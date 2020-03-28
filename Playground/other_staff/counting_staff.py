def test(A, B):
    return (5 * ((A + B) / 4 + B + A) / 4) - (A + B) / 4


if __name__ == "__main__":
    print(test(1, 1))
    print(test(100, 100))
    print(test(500, 500))

    print(test(5, 500))
    print(test(500, 5))

    print(test(300, 300))

    print(test(1000, 10000))
