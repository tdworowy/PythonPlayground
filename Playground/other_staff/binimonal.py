from math import factorial


def comb(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))


def binom_dist_cumulative(maxX, n, p):
    binom = 1
    pSuc = 1
    pFail = (1 - p) ** n
    prob = 0
    for x in range(0, maxX + 1, 1):
        prob = prob + binom * pSuc * pFail
        pSuc = pSuc * p
        pFail = pFail / (1 - p)
        binom = binom * (n - x) / (x + 1)
    return prob


if __name__ == "__main__":
    ratio = 1.09
    child_per_birth = 1
    p = ratio / (ratio + child_per_birth)

    n = 6
    res = sum(p ** k * (1 - p) ** (n - k) * comb(n, k) for k in range(3, 7))
    print(res)

    defective = 12
    size = 10

    p1 = binom_dist_cumulative(2, size, defective)
    p2 = 1 - binom_dist_cumulative(1, size, defective)

    (round(p1, 3))
    print(round(p2, 3))

    p_def = 1 / 3
    p_ok = 2 / 3
    tries = 5
    print(round((p_ok ** 4) * p_def, 3))

    print(round(1 / 3 ** 5), 3)

    print(round(sum([(p_ok ** (i - 1)) * p_def for i in range(1, tries + 1)]), 3))
