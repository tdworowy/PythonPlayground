import random


class CalculatePI:
    def __init__(self, count):
        self.count = count

    def pi(self):
        return 4 * sum(1 for _ in range(self.count) if
                       random.random() ** 2 + random.random() ** 2 < 1) / self.count


def main():
    pl = CalculatePI(10 ** 8)
    print(pl.pi())


if __name__ == '__main__':
    main()
