import sys

from Playground.my_utils.staff.timer3 import timer3

sys.setrecursionlimit(10000)


def memoize(f):
    call_cache = {}

    def _memoized(arg):
        try:
            return call_cache[arg]
        except KeyError:
            return call_cache.setdefault(arg, f(arg))

    return _memoized


@timer3
def fib1a(count):
    def _fib():
        a, b = 0, 1
        while 1:
            yield b
            a, b = b, a + b

    f = _fib()
    for i in range(count + 1):
        x = next(f)
    return x


@memoize
@timer3
def fib1b(count):
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
def fib2a(count):
    a, b = 0, 1
    for i in range(count):
        a, b = b, a + b

    return b


@memoize
@timer3
def fib2b(count):
    a, b = 0, 1
    for i in range(count):
        a, b = b, a + b

    return b


@timer3
def fib3a(count):
    if count < 2:
        return 1
    else:
        return fib3a(count - 1) + fib3a(count - 2)


@memoize
@timer3
def fib3b(count):
    if count < 2:
        return 1
    else:
        return fib3b(count - 1) + fib3b(count - 2)


if __name__ == "__main__":
    functions = [fib1a, fib1b, fib2a, fib2b, fib3a, fib3b]
    for i, f in enumerate(functions):
        print(f"{i} {f(90)}")
