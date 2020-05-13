def gcd(a, b):
    while a > 0 and b > 0:
        if a >= b:
            a = a % b
        else:
            b = b % a

    return max(a, b)


def lcm(a, b):
    return (a * b) / gcd(a, b)


print(lcm(2, 3))
print(lcm(10, 15))
print(lcm(35, 70))
