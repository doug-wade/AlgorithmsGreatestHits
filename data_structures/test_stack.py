from .stack import Stack
import random
import unittest

class StackTests(unittest.TestCase):

    def test_push_one(self):
        s = Stack()
        s.push(1)
        self.assertEqual(1, s._first.value)

    def test_push_two(self):
        s = Stack()
        s.push(1)
        s.push(2)
        self.assertTrue(s._first.value == 2 and s._first.next.value == 1)

    def test_pop_one(self):
        s = Stack()
        s.push(5)
        self.assertEqual(5, s.pop())

    def test_pop_two(self):
        s = Stack()
        s.push(3)
        s.push(2)
        s.pop()
        self.assertEqual(3, s.pop())

    def test_too_many_pops_dont_error(self):
        s = Stack()
        s.push(-1)
        s.pop()
        self.assertIsNone(s.pop())

    def test_peek(self):
        s = Stack()
        for i in range(10):
            new_int = random.randint(0,10000)
            s.push(new_int)
            self.assertEqual(s.peek(), new_int)

    def test_new_stack_pops_None(self):
        s = Stack()
        self.assertIsNone(s.pop())

    def test_new_stack_isEmpty(self):
        s = Stack()
        self.assertTrue(s.isEmpty())

    def test_emptied_stack_isEmpty(self):
        s = Stack()
        s.push("This is a string")
        s.pop()
        self.assertTrue(s.isEmpty())

    def test_length(self):
        s = Stack()
        for i in range(10):
            self.assertEqual(i, s.size())
            s.push(i)

        for i in range(10):
            self.assertEqual(10-i, s.size())
            s.pop()
