import math
import random

def rselect(array_to_search, n):
    """
    Returns the nth order statistic from the array provided.
    """
    return rselect_internal(array_to_search, n, 0, len(array_to_search))

def rselect_internal(search_array, n, start_index, end_index):
    """
    Recursively computes the nth order statistic between the start_index and
    the end_index.
    """
    assert(start_index >= 0 and end_index <= len(search_array))

    # Trivial case
    if start_index == end_index:
        return search_array[start_index]

    s = start_index
    e = end_index
    pp = math.floor(random.random() * (e - s)) + s
    comparisons = 0

    # Preprocessing to simplify tracking the sorted and unsorted portions
    # of the array that is being sorted.
    if pp != s:
        search_array[s], search_array[pp] = search_array[pp], search_array[s]

    c = search_array[s]
    j = s + 1
    i = s + 1

    while j < e:
        comparisons += 1
        if search_array[j] < c:
            search_array[j], search_array[i] = search_array[i], search_array[j]
            i += 1
        j += 1

    # Put the pivot back
    search_array[s], search_array[i - 1] = search_array[i - 1], search_array[s]

    # The pivot is what we're looking for
    if i - (s + 1) == n:
        return search_array[i - 1]
    if i - 1 > n:
        return rselect_internal(search_array, n, s, i - 1)
    else:
        return rselect_internal(search_array, n - i, i, e)

def rselect_from_file(file_path, n):
    """
    Performs Randomized select on a text file that contains an array containing
    a single element per line.
    """
    return rselect([int(line) for line in open(file_path)], n)
