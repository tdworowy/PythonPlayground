import sys

from Playground.my_utils.staff.timer3 import timer3

sys.setrecursionlimit(10000)


@timer3
def fib1(count):
    def _fib():
        a, b = 0, 1
        while 1:
            yield b
            a, b = b, a + b

    f = _fib()
    for i in range(count + 1):
        x = next(f)
    return x


@timer3
def fib2(count):
    a, b = 0, 1
    for i in range(count):
        a, b = b, a + b

    return b


@timer3
def fib3(count):
    if count < 2:
        return 1
    else:
        return fib3(count - 1) + fib3(count - 2)


def memoize(f):
    call_cache = {}

    def _memoized(arg):
        try:
            return call_cache[arg]
        except KeyError:
            return call_cache.setdefault(arg, f(arg))

    return _memoized


@memoize
@timer3
def fib4(count):
    if count < 2:
        return 1
    else:
        return fib4(count - 1) + fib4(count - 2)


@memoize
@timer3
def fib5(count):
    if count < 2:
        return 1
    else:
        return fib5(count - 1) + fib5(count - 2)


if __name__ == "__main__":
    functions = [fib1, fib2, fib3, fib4, fib4, fib5, fib5]
    for i, f in enumerate(functions):
        print(f"{i} {f(35)}")
