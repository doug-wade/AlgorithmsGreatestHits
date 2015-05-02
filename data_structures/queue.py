class Queue:
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
