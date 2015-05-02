import random
import unittest
from .selection_sort import selection_sort, find_min

class SelectionSortTests(unittest.TestCase):
    def setUp(self):
        self.list_of_ints = []
        for i in range(5000):
            next_int = random.randint(0,10000)
            self.list_of_ints.append(next_int)

    def test_find_min(self):
        self.assertEqual(min(self.list_of_ints), self.list_of_ints[find_min(0, self.list_of_ints)])

    def test_selection_sort(self):
        self.assertEqual(sorted(self.list_of_ints), selection_sort(self.list_of_ints))
