import sys


def odd(number):
    return number % 2 is not 0


def half(number):
    return number // 2


def multi(number1, number2):
    if number1 == 1: return number2
    result = multi(half(number1), number2 + number2)
    if odd(number1): result = result + number2
    return result


if __name__ == "__main__":
    sys.setrecursionlimit(20000)
    # print(multi(9,9))
    # # print(multi(99, 99))
    print(multi(2, 2))
    print(multi(4, 4))
    print(multi(5, 5))