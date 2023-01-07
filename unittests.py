import unittest
from mathematical_operations import *

class TestMathematicalOperations(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(my_sum(1, 2), 3)
        self.assertEqual(my_sum(1, 2, 7), 10)

    def test_prod(self):
        self.assertEqual(my_prod(1, 2), 2)
        self.assertEqual(my_prod(1, 2, 0), 0)


if __name__ == '__main__':
    unittest.main()
