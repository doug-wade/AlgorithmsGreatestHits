import random
import unittest

class stack:
    """
    A simple implementation of a stack.
    """

    def __init__(self):
        """
        Initializes an empty stack.
        """
        self._first = None
        self.length = 0


    class Node:
        """
        A single element of the linked list.
        """
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    def isEmpty(self):
        """
        Returns True if the list is empty, False otherwise.
        """
        if (self._first == None):
            return True
        return False

    def peek(self):
        """
        Peeks at the value of the item on the top of the stack (the most recent
        value added to the stack).
        """
        return self._first.value

    def pop(self):
        """
        Pops the most recent value added to the stack off the top of the stack
        """
        if (self.isEmpty()):
            return None
        self.length -= 1
        oldfirst = self._first
        self._first = oldfirst.next
        return oldfirst.value

    def push(self, val):
        """
        Adds a value to the top of the stack.
        """
        self.length += 1
        self._first = self.Node(val, self._first)

    def size(self):
        """
        Returns the number of items currently in the stack.
        """
        return self.length

class StackTests(unittest.TestCase):

    def test_push_one(self):
        s = stack()
        s.push(1)
        self.assertEqual(1, s._first.value)

    def test_push_two(self):
        s = stack()
        s.push(1)
        s.push(2)
        self.assertTrue(s._first.value == 2 and s._first.next.value == 1)

    def test_pop_one(self):
        s = stack()
        s.push(5)
        self.assertEqual(5, s.pop())

    def test_pop_two(self):
        s = stack()
        s.push(3)
        s.push(2)
        s.pop()
        self.assertEqual(3, s.pop())

    def test_too_many_pops_dont_error(self):
        s = stack()
        s.push(-1)
        s.pop()
        self.assertIsNone(s.pop())

    def test_peek(self):
        s = stack()
        for i in range(10):
            new_int = random.randint(0,10000)
            s.push(new_int)
            self.assertEqual(s.peek(), new_int)

    def test_new_stack_pops_None(self):
        s = stack()
        self.assertIsNone(s.pop())

    def test_new_stack_isEmpty(self):
        s = stack()
        self.assertTrue(s.isEmpty())

    def test_emptied_stack_isEmpty(self):
        s = stack()
        s.push("This is a string")
        s.pop()
        self.assertTrue(s.isEmpty())

    def test_length(self):
        s = stack()
        for i in range(10):
            self.assertEqual(i, s.size())
            s.push(i)

        for i in range(10):
            self.assertEqual(10-i, s.size())
            s.pop()

if __name__ == '__main__':
    unittest()