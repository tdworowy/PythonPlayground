from functools import reduce
if __name__ == "__main__":
    r1 = reduce((lambda x, y: x + y), [1, 2, 3, 4, 5])
    r2 = reduce((lambda x, y: x * y), [1, 2, 3, 4, 5])

    print(r1)
    print(r2)
