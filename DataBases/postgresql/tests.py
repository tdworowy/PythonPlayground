from postgresConection import postgresConection
from psycopg2.tests import unittest


class Tests(unittest.TestCase):

    def setUp(self):
        self.con = postgresConection("NoSql","User","test10")


    def test_conection(self):
        self.assertTrue(self.con is not None)

if __name__ == '__main__':
      unittest.main()
