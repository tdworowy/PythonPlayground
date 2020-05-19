def fast_modular_exponentiation_(b, k, m):
    """Only for (b ** 2) **k"""
    for i in range(k):
        b = (b * b) % m
    return b


def fast_modular_exponentiation(b, e, m):
    """for all K"""
    n = ""
    result = 1
    while e != 0:
        n = n + str(e % 2)
        e = int(e // 2)
    for i in range(len(n)):
        if n[i] == '1':
            result *= fast_modular_exponentiation_(b, i, m)
        result = result % m
    return result


print(fast_modular_exponentiation(7, 128, 11))
print(fast_modular_exponentiation(7, 127, 11))
