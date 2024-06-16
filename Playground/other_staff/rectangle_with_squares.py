def gcd(a, b):
    while a > 0 and b > 0:
        if a >= b:
            a = a % b
        else:
            b = b % a

    return max(a, b)


def squares(n, m):
    _gtc = gcd(n, m)
    if _gtc == 1:
        return n * m
    else:
        return n * m / _gtc**2


assert squares(2, 2) == 1
assert squares(6, 10) == 15
