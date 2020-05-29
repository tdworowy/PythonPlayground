import sys

if __name__ == "__main__":

    sys.setrecursionlimit(10000)


    def fib1(n: int) -> int:
        if n == 1 or n == 2:
            return 1
        else:
            return fib1(n - 1) + fib1(n - 2)


    def fib2(n: int) -> int:
        a, b = 0, 1
        for i in range(1, n):
            a, b = b, a + b
        return b


    print(fib2(12))
    print(fib2(10))
    print(fib2(1000))
