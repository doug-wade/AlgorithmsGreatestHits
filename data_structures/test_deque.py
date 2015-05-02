from .deque import Deque
import random
import unittest

class dequeTests(unittest.TestCase):
    def test_append_one(self):
        d = Deque()
        d.append("this is the last value")
        self.assertIsNone(d._first.prev, d._last.next)
        self.assertEqual(d._first.value, d._last.value,
            "this is the last value")
        self.assertEqual(d.size(), 1)

    def test_append_two(self):
        d = Deque()
        d.append(1)
        d.append(2)
        self.assertIsNone(d._first.prev, d._last.next)
        self.assertEqual(d._first.next, d._last, 2)
        self.assertEqual(d._last.prev, d._first, 1)
        self.assertEqual(d.size(), 2)

    def test_prepend_one(self):
        d = Deque()
        d.prepend("this is the first value")
        self.assertIsNone(d._first.prev, d._last.next)
        self.assertEqual(d._first.value, d._last.value,
            "this is the first value")
        self.assertEqual(d.size(), 1)

    def test_prepend_two(self):
        d = Deque()
        d.prepend(2)
        d.prepend(1)
        self.assertIsNone(d._first.prev, d._last.next)
        self.assertEqual(d._first.next, d._last, 2)
        self.assertEqual(d._last.prev, d._first, 1)
        self.assertEqual(d.size(), 2)

    def test_pop_first(self):
        comp_list = []
        d = Deque()
        for i in range(10):
            new_int = random.randint(0,10000)
            comp_list.append(new_int)
            d.append(new_int)
        self.assertEqual(d.size(), 10)
        for i in range(len(comp_list)):
            self.assertEqual(comp_list[i], d.pop_first())
        self.assertEqual(d.size(), 0)

    def test_pop_last(self):
        comp_list = []
        d = Deque()
        for i in range(10):
            new_int = random.randint(0,10000)
            comp_list.append(new_int)
            d.prepend(new_int)
        self.assertEqual(d.size(), 10)
        for i in range(len(comp_list)):
            self.assertEqual(comp_list[i], d.pop_last())
        self.assertEqual(d.size(), 0)
