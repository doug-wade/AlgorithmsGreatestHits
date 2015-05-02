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
