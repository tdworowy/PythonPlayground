def extended_gcd(a: int, b: int) -> tuple:
    assert a >= 0 and b >= 0 and a + b > 0

    if b == 0:
        d, x, y = a, 1, 0
    else:
        (d, p, q) = extended_gcd(b, a % b)
        x = q
        y = p - q * (a // b)

    return d, x, y


def diophantine(a: int, b: int, c: int) -> tuple:
    ex_gcd = extended_gcd(a, b)
    assert c % ex_gcd[0] == 0
    z = c / ex_gcd[0]
    return ex_gcd[1] * z, ex_gcd[2] * z


eq1 = (6, 9, 27)
eq2 = (5, 3, 22)
print(diophantine(*eq1))
print(diophantine(*eq2))
