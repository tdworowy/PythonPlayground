import sys


def odd(number):
    return number % 2 is not 0


def half(number):
    return number // 2


def accumulate_multi(res, number1, number2):
    while 1:
        if odd(number1):
            res = res + number2
            if number1 == 1: return number2
        number1 = half(number1)
        number2 = number2 + number2


def multi(number1, number2):
    if number2 > number1:
        number1, number2 = number2, number1
    while not odd(number1):
        number2 = number2 + number2
        number1 = half(number1)
    if number1 == 1: return number2
    return accumulate_multi(number2, half(number1 - 1), number2 + number2)


if __name__ == "__main__":
    sys.setrecursionlimit(20000)
    print(multi(9,9))
    print(multi(99, 99))
    print(multi(2, 2))
    print(multi(4, 4))
    print(multi(5, 5))
    print(multi(5, 999))
    print(multi(999, 5))
