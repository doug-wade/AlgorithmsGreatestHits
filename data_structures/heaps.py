from heapq import *

class maxheapq:
    """
    Simple wrappers for the built-in heapq module for ease of use.
    """
    def __init__(self, L=[]):
        """
        Set up as a class to prevent errors in negation.
        """
        M = []
        for val in L:
            M.append(-1 * val)
        heapify(M)
        self._h = M
        self._l = len(M)

    def length(self):
        """
        Returns the number of elements in the heap.
        """
        return(self._l)

    def pop(self):
        """
        Pops the maximum value off the heap.
        """
        self._l -= 1
        return(-1 * heappop(self._h))

    def push(self, item):
        """
        Pushes a new element onto the heap.
        """
        self._l += 1
        heappush(self._h, -1 * item)

    def pushpop(self, item):
        """
        Pushes a new element onto the heap, then pops the maximum value off.
        """
        self.push(item)
        return(self.pop())


class minheapq:
    def __init__(self, L=[]):
        """
        A simple wrapper for heapq to match my intuitions about how a heap would be
        implemented/to match max
        """
        heapify(L)
        self._h = L
        self._l = len(L)

    def length(self):
        """
        Returns the number of elements in the heap.
        """
        return(self._l)

    def pop(self):
        """
        Pops the minimum value off the heap.
        """
        self._l -= 1
        return(heappop(self._h))

    def push(self, item):
        """
        Pushes as new value onto the heap.
        """
        self._l += 1
        heappush(self._h, item)

    def pushpop(self, item):
        """
        Pushes a new item off the heap, then pops the minimum element off the 
        heap.
        """
        self.push(item)
        return(self.pop())

class tuple_min_heapq:
    def __init__(self):
        """
        A simple wrapper for heapq to match my intuitions about how a heap would be
        implemented/to match the other heaps.
        """
        self._h = []
        self._l = 0
        self._d = {}

    def __getitem__(self, key):
        return self._d[key]

    def contains(self, key):
        """
        Returns True if a key is in the heap, False otherwise.
        """
        if key in self._d:
            return True
        else:
            return False

    def delete(self, key):
        if key in self._d.keys():
            del self._d[key]
            self._h[i] = self._h[-1]
            self._h.pop()
            heapify(self._h)

    def length(self):
        """
        Returns the number of elements in the heap.
        """
        return(self._l)

    def pop(self):
        """
        Pops the minimum value off the heap.
        """
        self._l -= 1
        inter_tuple = heappop(self._h)
        heapify(self._h)
        del self._d[inter_tuple[1]]
        return(inter_tuple[1], inter_tuple[0])

    def push(self, key, value):
        """
        Pushes as new value onto the heap.
        """
        self._l += 1
        self._d[key] = value
        heappush(self._h, (value, key))
        heapify(self._h)

    def pushpop(self, key, value):
        """
        Pushes a new item off the heap, then pops the minimum element off the 
        heap.
        """
        self.push(key, value)
        return(self.pop())

    def update(self, key, value):
        """
        Updates the value for a given key.
        """
        if self._d[key] != value:
            self._d[key] = value
            self._h = [(v, k) if (k != key) else (value, key) for (v, k) in self._h]
            heapify(self._h)