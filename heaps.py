"""
Simple wrappers for the built-in heapq module for ease of use.
"""

class maxheapq:
    def __init__(self, L=[]):
        """
        Set up as a class to prevent errors in negation.
        """
        M = []
        for val in L:
            M.append(-1 * val)
        heapq.heapify(M)
        self._h = M
        self._l = len(M)

    def length(self):
        """
        Returns the number of elements in the heap.
        """
        # For this particular use case, I'll be checking the length much more
        # often than I'll be changing the contents, so doing the bookeeping 
        # will save time over repeatedly calling len().
        return(self._l)

    def pop(self):
        """
        Pops the maximum value off the heap.
        """
        self._l -= 1
        return(-1 * heapq.heappop(self._h))

    def push(self, item):
        """
        Pushes a new element onto the heap.
        """
        self._l += 1
        heapq.heappush(self._h, -1 * item)

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
        implemented/to match maxheapq.
        """
        heapq.heapify(L)
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
        return(heapq.heappop(self._h))

    def push(self, item):
        """
        Pushes as new value onto the heap.
        """
        self._l += 1
        heapq.heappush(self._h, item)

    def pushpop(self, item):
        """
        Pushes a new item off the heap, then pops the minimum element off the 
        heap.
        """
        self.push(item)
        return(self.pop())

class tuple_min_heapq():
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
        inter_tuple = heapq.heappop(self._h)
        del self._d[inter_tuple[1]]
        return(inter_tuple[1], inter_tuple[0])

    def push(self, key, value):
        """
        Pushes as new value onto the heap.
        """
        self._l += 1
        self._d[key] = value
        heapq.heappush(self._h, (value, key))

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
            self._l = [(k,v) if (k != key) else (key, value) for (k, v) in self._l]