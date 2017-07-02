#test
import unittest


def add(x,y):
    return x+y



class Tests(unittest.TestCase):
    def testAdd1(self):
       assert add(1,2) == 3

    def testAdd2(self):
        assert add(0, 0) == 0

    def testAdd2(self):
        assert add(10, -2) == 8

    def testLetters(self):
        assert add('x', 'z') == 'xz'



if __name__ == '__main__':
    test_program = unittest.main()