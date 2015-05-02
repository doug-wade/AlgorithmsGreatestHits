import math

def binary_search(array_to_search, elem):
    """
    Performs binary search to find elem in array_to_search.  Returns the index
    of elem if elem is in array_to_search, -1 otherwise.
    """
    return binary_search_r(array_to_search, elem, 0, len(array_to_search))

def binary_search_r(array_to_search, elem, start, end):
    """
    Recursive helper function for binary_search
    """
    if start == end:
        if elem == array_to_search[start]:
            return start
        else:
            return -1

    if start > end:
        return -1

    mid = math.floor((end-start)/2) + start
    if elem < array_to_search[mid]:
        return binary_search_r(array_to_search, elem, start, mid - 1)
    elif elem > array_to_search[mid]:
        return binary_search_r(array_to_search, elem, mid + 1, end)
    elif elem == array_to_search[mid]:
        return mid
