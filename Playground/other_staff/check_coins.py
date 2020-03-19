import itertools


def find_biggest_that_can_be_pay():
    res = []
    for c in range(1, 100):
        for comb in list(itertools.product(range(0, 15), range(0, 15))):
            if 5 * comb[0] + 7 * comb[1] == c:
                break
        else:
            res.append(c)


def change(amount: int):
    for comb in list(itertools.product(range(0, 100), range(0, 100))):
        if 5 * comb[0] + 7 * comb[1] == amount:
            res = "5," * comb[0]
            res += "7," * comb[1]
            return [int(x) for x in res.split(",")[:-1]]


if __name__ == "__main__":
    print(change(1000))
