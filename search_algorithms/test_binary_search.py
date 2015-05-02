import unittest
import random
from .binary_search import binary_search

class binary_search_test(unittest.TestCase):
    def setUp(self):
        self.oddNums = [ 1, 3, 5, 7, 9 ]
        self.randNums = sorted([ random.randint(0, 10000) for i in range(100000) ])

    def test_not_found_returns_minus_one(self):
        self.assertEqual(binary_search(self.oddNums, 2), -1)

    def test_find_odd_num(self):
        self.assertEqual(binary_search(self.oddNums, 5), 2)

    def test_find_rand_num(self):
        randChoice = random.choice(self.randNums)
        index = binary_search(self.randNums, randChoice)
        self.assertEqual(self.randNums[index], randChoice)
