from .queue import Queue
import random
import unittest

class QueueTests(unittest.TestCase):
    def test_enqueue_one(self):
        q = Queue()
        q.enqueue(1)
        self.assertTrue(q._first.value == 1 and q._last.value == 1)

    def test_enqueue_two(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        self.assertTrue(q._first.value == 1 and q._last.value == 2)

    def test_dequeue_one(self):
        q = Queue()
        q.enqueue("this is a string")
        self.assertEqual(q.dequeue(), "this is a string")

    def test_dequeue_two(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        self.assertTrue(q.dequeue() == 1 and q.dequeue() == 2)

    def test_too_many_dequeues_dont_error(self):
        q = Queue()
        q.enqueue("this is a string")
        q.dequeue()
        self.assertIsNone(q.dequeue())

    def test_peek(self):
        q = Queue()
        for i in range(10):
            new_int = random.randint(0,10000)
            q.enqueue(new_int)
            self.assertEqual(q.peek(), new_int)

    def test_new_queue_dequeues_None(self):
        q = Queue()
        self.assertIsNone(q.dequeue())

    def test_new_queue_isEmpty(self):
        q = Queue()
        self.assertTrue(q.isEmpty())

    def test_emptied_stack_isEmpty(self):
        q = Queue()
        q.enqueue("This is a string")
        q.dequeue()
        self.assertTrue(q.isEmpty())

    def test_length(self):
        q = Queue()
        for i in range(10):
            self.assertEqual(i, q.size())
            q.enqueue(i)

        for i in range(10):
            self.assertEqual(10-i, q.size())
            q.dequeue()
