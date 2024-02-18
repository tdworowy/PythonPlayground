'''Find primes'''
from Playground.my_utils.staff.timer3 import timer3


def primes_sieve(limit: int) -> iter:
    a = [True] * limit
    a[0] = a[1] = False

    for (i, is_prime) in enumerate(a):
        if is_prime:
            yield i
            for n in range(i * i, limit, i):
                a[n] = False

@timer3
def is_prime1(number: int) -> bool:
    return number in list(primes_sieve(number))

@timer3
def is_prime2(number: int) -> int:
    if number & 1 == 0:
        return 2
    d = 3
    while d * d <= number:
        if number % d == 0:
            return d
        d = d + 2
    return 0


if __name__ == "__main__":
    print(is_prime1(100000000))
    print(is_prime2(100000000))
