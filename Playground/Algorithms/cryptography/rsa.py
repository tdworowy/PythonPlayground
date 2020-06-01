def extended_euclid(a: int, b: int) -> tuple:
    if b == 0:
        return 1, 0
    (x, y) = extended_euclid(b, a % b)
    k = a // b
    return y, x - k * y


def invert_modulo(a: int, n: int) -> int:
    (b, x) = extended_euclid(a, n)
    if b < 0:
        b = (b % n + n) % n
    return b


def convert_to_int(message_str: str) -> int:
    res = 0
    for i in range(len(message_str)):
        res = res * 256 + ord(message_str[i])
    return res


def fast_modular_exponentiation_(b: int, k: int, m: int) -> int:
    for i in range(k):
        b = (b * b) % m
    return b


def fast_modular_exponentiation(b: int, e: int, m: int) -> int:
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


def convert_to_str(n):
    res = ""
    while n > 0:
        res += chr(n % 256)
        n //= 256
    return res[::-1]


def encrypt(message: str, modulo: int, exponent: int) -> int:
    return fast_modular_exponentiation(convert_to_int(message), exponent, modulo)


def decrypt(cipher_text: int, p: int, q: int, exponent: int) -> str:
    number = (p - 1) * (q - 1)
    d = invert_modulo(exponent, number)
    return convert_to_str(fast_modular_exponentiation(cipher_text, d, p * q))


if __name__ == "__main__":
    p = 1000000007
    q = 1000000009
    exponent = 23917
    modulo = p * q
    cipher_text = encrypt("test", modulo, exponent)
    message = decrypt(cipher_text, p, q, exponent)
    print(message)
