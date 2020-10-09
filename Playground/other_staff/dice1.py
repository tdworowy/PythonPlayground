import random

if __name__ == "__main__":
    res = []
    n = 10000000
    for i in range(n):
        roll = True
        j = 1
        while roll:
            x = random.randrange(1, 7)
            y = random.randrange(1, 7)
            if x < y:
                res.append(j)
                roll = False
            else:
                j += 1

    print(sum(res) / n)
    # print(res)
