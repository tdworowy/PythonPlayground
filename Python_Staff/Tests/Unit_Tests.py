# test
import unittest


def add(x, y):
    return x + y


class TestAdd(unittest.TestCase):
    def test_add_positive_integers(self):
        self.assertEquals(add(1, 2), 3)

    def test_add_zero(self):
        self.assertEquals(add(0, 0), 0)

    def test_add_one_negative(self):
        self.assertEquals(add(10, -2), 8)

    def test_add_two_negative(self):
        self.assertEquals(add(-2, -2), -4)

    def test_add_chars(self):
        self.assertEquals(add('x', 'z'), 'xz')


if __name__ == '__main__':
    unittest.main()
