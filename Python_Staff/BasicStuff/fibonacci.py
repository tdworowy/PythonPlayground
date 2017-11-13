import sys

sys.setrecursionlimit(10000)


def fib(n):
    if n == 1 or n == 2:
        return 1

    else:
        return fib(n - 1) + fib(n - 2)


def fib2(n):
    a, b = 0, 1
    for i in range(1, n):
        a, b = b, a + b
    return b


print(fib2(1000000))
