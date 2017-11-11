import sys

sys.setrecursionlimit(10000)


def factorial(n):
    if n == 0 or n == 1:
        return 1

    else:
        return n * factorial(n - 1)


def factorial2(n):
    result = 1
    while n > 1:
        result = result * n
        n -= 1
    return result


print(factorial(10))
print(factorial2(10))
