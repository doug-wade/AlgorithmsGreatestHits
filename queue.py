import random
import unittest

class queue:
    """
    A simple implementation of a queue.
    """

    def __init__(self):
        """
        Initializes an empty queue.
        """
        self._first = None
        self._last = None
        self._length = 0

    class Node:
        """
        A single element of the linked list.
        """
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    def isEmpty(self):
        """
        Returns True is the queue is empty, False otherwise.
        """
        return self._first == None

    def size(self):
        """
        Returns the number of elements in the queue currently
        """
        return self._length

    def peek(self):
        """
        Returns the next value that would be returned by dequeue.
        """
        return self._last.value

    def dequeue(self):
        """
        Removes and returns the least-recently-added node from the queue.
        """
        if (self._length == 0):
            return None

        self._length -= 1
        oldfirst = self._first
        self._first = oldfirst.next
        if (self.isEmpty()):
            self._last = None
        return oldfirst.value

    def enqueue(self, value):
        """
        Adds a value to the queue.
        """
        self._length += 1
        oldlast = self._last
        self._last = self.Node(value, None)
        if (self.isEmpty()):
            self._first = self._last
        else:
            oldlast.next = self._last

class QueueTests(unittest.TestCase):

    def test_enqueue_one(self):
        q = queue()
        q.enqueue(1)
        self.assertTrue(q._first.value == 1 and q._last.value == 1)

    def test_enqueue_two(self):
        q = queue()
        q.enqueue(1)
        q.enqueue(2)
        self.assertTrue(q._first.value == 1 and q._last.value == 2)

    def test_dequeue_one(self):
        q = queue()
        q.enqueue("this is a string")
        self.assertEqual(q.dequeue(), "this is a string")

    def test_dequeue_two(self):
        q = queue()
        q.enqueue(1)
        q.enqueue(2)
        self.assertTrue(q.dequeue() == 1 and q.dequeue() == 2)

    def test_too_many_dequeues_dont_error(self):
        q = queue()
        q.enqueue("this is a string")
        q.dequeue()
        self.assertIsNone(q.dequeue())

    def test_peek(self):
        q = queue()
        for i in range(10):
            new_int = random.randint(0,10000)
            q.enqueue(new_int)
            self.assertEqual(q.peek(), new_int)

    def test_new_queue_dequeues_None(self):
        q = queue()
        self.assertIsNone(q.dequeue())

    def test_new_queue_isEmpty(self):
        q = queue()
        self.assertTrue(q.isEmpty())

    def test_emptied_stack_isEmpty(self):
        q = queue()
        q.enqueue("This is a string")
        q.dequeue()
        self.assertTrue(q.isEmpty())

    def test_length(self):
        q = queue()
        for i in range(10):
            self.assertEqual(i, q.size())
            q.enqueue(i)

        for i in range(10):
            self.assertEqual(10-i, q.size())
            q.dequeue()

if (__name__ == '__main__'):
    unittest()