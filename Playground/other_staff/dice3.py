import random

if __name__ == "__main__":
    n = 10000
    mean = sum([random.randrange(1, 7) for i in range(n)]) / n
    print(mean)
