import unittest

from Playground.python_staff.Functions_ import numbers_pair_sum


class TestStringMethods(unittest.TestCase):
    list8 = [-1, 1, 4, 4, 1, 20]
    list9 = [0, 8]

    def test_1(self):
        list1 = [1, 2, 3, 4, 5]
        self.assertTrue(numbers_pair_sum.find_pair(list1, 8))

    def test_2(self):
        list1 = [7, 2, 3, 4, 4]
        self.assertTrue(numbers_pair_sum.find_pair(list1, 8))

    def test_3(self):
        list1 = [11, 2, 3, 4, 4]
        self.assertTrue(numbers_pair_sum.find_pair(list1, 8))

    def test_4(self):
        list1 = [11, 2, 3, 4, 4, 22]
        self.assertTrue(numbers_pair_sum.find_pair(list1, 8))

    def test_5(self):
        list1 = [1, 1, 1, 1, 1, 22]
        self.assertFalse(numbers_pair_sum.find_pair(list1, 8))

    def test_6(self):
        list1 = [-1, 1, 1, 4, 1, 9]
        self.assertTrue(numbers_pair_sum.find_pair(list1, 8))

    def test_7(self):
        list1 = [-1, 1, 4, 4, 1, 20]
        self.assertTrue(numbers_pair_sum.find_pair(list1, 8))

    def test_8(self):
        list1 = [0, 8]
        self.assertTrue(numbers_pair_sum.find_pair(list1, 8))

    def test_9(self):
        notList = "Test"
        self.assertEqual(numbers_pair_sum.find_pair(notList, 8), "First argument must be list")

    def test_10(self):
        list1 = [0]
        self.assertEqual(numbers_pair_sum.find_pair(list1, 8), "List must have at leas 2 elements")

    def test_11(self):
        list1 = [1, 2]
        self.assertEqual(numbers_pair_sum.find_pair(list1, "A"), "Second argument must be the int")

    def test_12(self):
        list1 = [1, 2]
        self.assertEqual(numbers_pair_sum.find_pair(list1, [1, 2, 3]), "Second argument must be the int")


if __name__ == '__main__':
    unittest.main()
