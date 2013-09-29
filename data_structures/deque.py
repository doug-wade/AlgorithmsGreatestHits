import unittest
import random

class Deque:
    """
    An implementation of a deck that allows pushing and popping from both the
    front and the back of a doubly linked list.
    """
    def __init__(self):
        """
        Initializes an empty deque.
        """
        self._length = 0
        self._first = None
        self._last = None

    class Node:
        """
        A single element of the linked list.
        """
        def __init__(self, value, prev=None, next=None):
            self.value = value
            self.next = next
            self.prev = prev

    def append(self, value):
        """
        Adds a new value to the back of the deque.
        """
        oldlast = self._last
        new_node = self.Node(value, oldlast, None)
        self._last = new_node
        if self._length == 0:
            self._first = new_node
        else:
            oldlast.next = new_node
        self._length += 1

    def pop_first(self):
        """
        Removes the value from the front of the deque.
        """
        oldfirst = self._first
        self._first = oldfirst.next
        if self._first:
            self._first.prev = None
        self._length -= 1
        return oldfirst.value

    def pop_last(self):
        """
        Removes the value from the back of the deque.
        """
        oldlast = self._last
        self._last = oldlast.prev
        if self._last:
            self._last.next = None
        self._length -= 1
        return oldlast.value

    def prepend(self, value):
        """
        Adds a new value to the front of the deque.
        """
        oldfirst = self._first
        new_node = self.Node(value, None, oldfirst)
        self._first = new_node
        if self._length == 0:
            self._last = new_node
        else:
            oldfirst.prev = new_node
        self._length += 1

    def size(self):
        """
        Returns the number of elements in the deck.
        """
        return self._length

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


if __name__ == '__main__':
    unittest()