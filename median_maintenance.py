import heapq

class maxheapq:
    """
    Set up as a class to prevent errors in negation.
    """
    def __init__(self, L=[]):
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
    """
    A simple wrapper for heapq to match my intuitions about how a heap would be
    implemented/to match maxheapq.
    """
    def __init__(self, L=[]):
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


def sum_medians(medians):
    """
    Takes a list of integers; returns a sum of all elements.
    """
    sum_of_medians = 0
    for m in medians:
        sum_of_medians += m
    return sum_of_medians

def median_maintenance(file_location):
    """
    Keeps track of the median at all times in a stream of integers.
    """
    bottom_half, top_half, medians = maxheapq(), minheapq(), []
    max_bottom, min_top, count_ints = 0, 0, 0

    f = open(file_location)
    for line in f:
        new_int = int(line)

        # Don't let the initialization values get in the stream.
        if count_ints < 2:
            if count_ints < 1:
                medians.append(new_int)
                min_top = new_int
                count_ints += 1
            else:
                count_ints += 1
                if new_int > min_top:
                    max_bottom = min_top
                    min_top = new_int
                else:
                    max_bottom = new_int
                medians.append(max_bottom)
            continue


        # Put the new int in the right place
        if new_int > min_top:
            top_half.push(new_int)
        elif new_int < max_bottom:
            bottom_half.push(new_int)
        # The new int is a/the new median; correct imbalances if possible
        elif top_half.length() > bottom_half.length():
            bottom_half.push(max_bottom) # new_int is greater than max_bottom
            max_bottom = new_int
        else:
            top_half.push(min_top)
            min_top = new_int
        
        # Rebalance the heaps
        if bottom_half.length() > top_half.length() + 1:
            top_half.push(min_top)
            min_top = max_bottom
            max_bottom = bottom_half.pop()
        elif top_half.length() > bottom_half.length() + 1:
            bottom_half.push(max_bottom)
            max_bottom = min_top
            min_top = top_half.pop()

        # Get the new median and add it to the median list
        if (bottom_half.length() + top_half.length()) % 2:
            if bottom_half.length() > top_half.length():
                medians.append(max_bottom)
            else:
                medians.append(min_top)
        else:
            medians.append(max_bottom)

    return(sum_medians(medians))

print(median_maintenance('./data/Median.txt'))
#median_maintenance('./data/Median.txt')