import random

if __name__ == "__main__":
    n = 100000
    mean = sum([random.randrange(1, 7) for i in range(n)]) / n
    print(mean)

    print(sum([1, 2, 3, 4, 5, 6]) / 6)
