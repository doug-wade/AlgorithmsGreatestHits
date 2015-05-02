class Stack:
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
