import random

if __name__ == "__main__":
    x = random.choice(["a", "b", "c"])
    print(x)
    test = "a;b;c"
    print(test.split(";"))

    dir(test)
    m = [[1, 2, 3], ["a", "b", "c"], [3, 5, 6]]
    print(m)
    print(m[1][2])

    D = {"a": 1, "b": 2, "c": 3}
    ks = list(D.keys())
    print(ks)
    ks.sort()
    print(ks)
    for key in ks:
        print(key, "=>", D[key])

    ks2 = D.keys()
    print(ks2)
    for x in range(1, 40):
        ks.append(x**2)

    print(ks)
    dir(range)
