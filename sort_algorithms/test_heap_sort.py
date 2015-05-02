import unittest
import random
from .heap_sort import heap_sort

class HeapSortTests(unittest.TestCase):
    def setUp(self):
        self.list_of_ints = [ random.randint(0,10000) for i in range(100000) ]

    def test_heap_sort_int(self):
        self.assertEqual(sorted(self.list_of_ints), heap_sort(self.list_of_ints))

    def test_heap_sort_int_reverse(self):
        self.assertEqual(sorted(self.list_of_ints, reverse=True), heap_sort(self.list_of_ints, True))
