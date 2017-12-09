import random
from math import sqrt
from random import random as r
from time import time


class CalculatePI:
    def __init__(self, count):
        self.count = count

    def pi(self):
        return 4 * sum(1 for _ in range(self.count) if
                       random.random() ** 2 + random.random() ** 2 < 1) / self.count


def distance(a, b, c, d):
    return sqrt(abs((a - c) ** 2 + (b - d) ** 2))
    total = 0
    trials = 0
    end = 10 + time()
    while time() < end:
        total += distance(r(), r(), r(), r())
        trials += 1
    print("Answer:", total / trials)


def main():
    pl = CalculatePI(10 ** 8)
    print(pl.pi())


if __name__ == '__main__':
    main()
