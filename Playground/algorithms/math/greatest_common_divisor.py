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
    numbers = [981982, 23232, 232323, 224242, 23232323, 2930290392039, 232323]
    g = numbers[0]
    for number in numbers[1::]:
        g = extended_gcd(g, number)[0]
    print(g)
