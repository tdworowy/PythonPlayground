from psycopg2.tests import unittest

from Data_bases.postgresql.postgresConection import postgresConection


class Tests(unittest.TestCase):

    def setUp(self):
        self.con = postgresConection("NoSql","User","test10")


    def test_conection(self):
        self.assertTrue(self.con is not None)

if __name__ == '__main__':
      unittest.main()
