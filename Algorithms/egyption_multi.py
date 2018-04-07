import unittest


def odd(number):
    return number % 2 is not 0


def half(number):
    return number // 2


def accumulate_multi(res, number1, number2):
    while 1:
        if odd(number1):
            res = res + number2
            if number1 == 1: return res
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


class MultiTests(unittest.TestCase):
    args = []

    def test_multiplication(self):
        for tuple_ in self.args:
            print("%s * %s = %s" % tuple_)
            res =multi(tuple_[0], tuple_[1])
            print("RESULT: %s" % res)
            assert res == tuple_[2]


if __name__ == "__main__":
    args = [(9, 9, 81),
            (99, 99, 9801),
            (1, 99, 99),
            (99, 1, 99),
            (1, 1, 1),
            (5, 9, 45),
            (9, 5, 45)
            ]

    MultiTests.args = args
    unittest.main()
