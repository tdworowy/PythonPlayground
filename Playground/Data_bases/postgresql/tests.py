from psycopg2.tests import unittest

from Data_bases.postgresql.PostgresConnection import PostgresConnection


class Tests(unittest.TestCase):

    def setUp(self):
        self.con = PostgresConnection("NoSql", "User", "test10")

    def test_connection(self):
        self.assertTrue(self.con is not None)


if __name__ == '__main__':
    unittest.main()
