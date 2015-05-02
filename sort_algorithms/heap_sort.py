from heapq import *

def heap_sort(int_list, reverse=False):
    """
    An implementation of heap sort.
    """
    heap = []
    factor = -1 if reverse else 1
    for integer in int_list:
        heappush(heap, factor * integer)
    return [ factor * heappop(heap) for _ in range(len(int_list)) ]
