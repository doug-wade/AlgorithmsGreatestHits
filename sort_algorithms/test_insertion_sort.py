import unittest
import random
from .insertion_sort import insertion_sort

class InsertionSortTests(unittest.TestCase):
    def setUp(self):
        self.list_of_ints = []
        for i in range(1000):
            next_int = random.randint(0,10000)
            self.list_of_ints.append(next_int)

    def test_insertion_sort(self):
        self.assertEqual(sorted(self.list_of_ints), insertion_sort(self.list_of_ints))

    def test_insertion_sort_empty(self):
        self.assertEqual([], insertion_sort([]))

    def test_insertion_sort_single_elem(self):
        self.assertEqual([ 1 ], insertion_sort([ 1 ]))
