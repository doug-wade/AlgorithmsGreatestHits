import random
import unittest
from .quick_sort import quick_sort

class QuickSortTests(unittest.TestCase):
    def setUp(self):
        self.list_of_ints = []
        for i in range(100):
            next_int = random.randint(0,10000)
            self.list_of_ints.append(next_int)

    def test_quick_sort(self):
        self.assertEqual(sorted(self.list_of_ints), quick_sort(self.list_of_ints))
