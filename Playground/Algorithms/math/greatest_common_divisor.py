def extended_gcd(a: int, b: int) -> tuple:
    assert a >= 0 and b >= 0 and a + b > 0

    if b == 0:
        d, x, y = a, 1, 0
    else:
        (d, p, q) = extended_gcd(b, a % b)
        x = q
        y = p - q * (a // b)

    return d, x, y


if __name__ == "__main__":
    print(extended_gcd(10, 6))
    print(extended_gcd(7, 5))
    print(extended_gcd(391, 299))
    print(extended_gcd(239, 201))
