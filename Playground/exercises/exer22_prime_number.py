def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def is_prime(n):
    if n <= 1:
        return False
    x = [1 for i in range(2, n) if n % i == 0]
    if x:
        return False
    else:
        return True


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True


if __name__ == "__main__":
    for i in [3, 12, 5, 7]:
        if is_prime(i):
            print("Prime")
        else:
            print("Not Prime")
