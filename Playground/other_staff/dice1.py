import random

if __name__ == "__main__":
    res = []
    for i in range(10000000):
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

    print(sum(res) / 10000000)
    # print(res)
