import unittest
import random
from .merge_sort import merge_sort

class MergeSortTests(unittest.TestCase):
    def setUp(self):
        self.list_of_ints = []
        for i in range(100000):
            next_int = random.randint(0, 10000)
            self.list_of_ints.append(next_int)

    def test_merge_sort(self):
        self.assertEqual(sorted(self.list_of_ints), merge_sort(self.list_of_ints))

    def test_merge_sort_empty(self):
        self.assertEqual([], merge_sort([]))

    def test_merge_sort_single_elem(self):
        self.assertEqual([ 1 ], merge_sort([ 1 ]))
