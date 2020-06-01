def extended_gcd(a: int, b: int) -> tuple:
    assert a >= 0 and b >= 0 and a + b > 0

    if b == 0:
        d, x, y = a, 1, 0
    else:
        (d, p, q) = extended_gcd(b, a % b)
        x = q
        y = p - q * (a // b)

    return d, x, y


def chinese_remainder_theorem(n1, r1, n2, r2):
    (_, x, y) = extended_gcd(n1, n2)
    n = x * n1 * r2 + y * n2 * r1
    return n % (n1 * n2)


if __name__ == "__main__":
    print(chinese_remainder_theorem(686579304, 295310485, 26855093, 8217207))
