import random

if __name__ == "__main__":
    res = {5: 1, 10: 1, 6: 1, 3: 1, 8: 1, 4: 1, 7: 1, 2: 1, 9: 1, 11: 1, 12: 1}
    for i in range(100000):
        x = random.randrange(1, 7)
        y = random.randrange(1, 7)
        res[x + y] += 1
    print(res)
