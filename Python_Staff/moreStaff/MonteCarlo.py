import random


class calculatePI():
    def __init__(self, timesToRepeat):
        self.timesToRepeat = timesToRepeat

    def pi(self):
        return 4 * sum(1 for _ in range(self.timesToRepeat) if
                       random.random() ** 2 + random.random() ** 2 < 1) / self.timesToRepeat


def main():
    piCalc = calculatePI(10 ** 8)
    print(piCalc.pi())


if __name__ == '__main__':
    main()
