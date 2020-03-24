from math import sqrt
from itertools import islice, count


def is_prime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n) - 1)))


if __name__ == "__main__":
    for x in range(1, 1000000):
        y = (x ** 2) + x + 41
        if not is_prime(y):
            print(x)
            break
