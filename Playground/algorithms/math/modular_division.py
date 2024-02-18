def extended_gcd(a: int, b: int) -> tuple:
    assert a >= 0 and b >= 0 and a + b > 0

    if b == 0:
        d, x, y = a, 1, 0
    else:
        (d, p, q) = extended_gcd(b, a % b)
        x = q
        y = p - q * (a // b)

    return d, x, y


def divide(a: int, b: int, n: int) -> int:
    ex_gcd = extended_gcd(a, n)
    assert n > 1 and a > 0 and ex_gcd[0] == 1
    d, s, t = ex_gcd[0], ex_gcd[1], ex_gcd[2]
    s %= n
    x = (b * s) % n
    assert x >= 0
    return x
