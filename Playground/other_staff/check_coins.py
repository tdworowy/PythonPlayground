import itertools

if __name__ == "__main__":
    res = []
    for c in range(1, 100):
        for comb in list(itertools.product(range(0, 15), range(0, 15))):
            if 5 * comb[0] + 7 * comb[1] == c:
                break
        else:
            res.append(c)
    print(res)