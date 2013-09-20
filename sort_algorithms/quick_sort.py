import collections
import math
import numpy
import os
import random
import unittest

# An object to pass around the results
result = collections.namedtuple('result', ['array', 'comparisons'])

def partition(array_to_partition, start_index, end_index, partition_style):
    """
    There are various ways to choose a partition.  The function returns the
    index of the passed array that is to be used as the pivot point. The
    following options are available for sorting using the second parameter:
    f or first: returns 0
    l or last: returns the index of the last element of the array
    m or median: return the index of the median of the first, last, and middle
                 elements of the array
    r or random: returns a random element of the array
    """
    if partition_style.lower()[0] == "f":
        return start_index

    elif partition_style.lower()[0] == "l":
        return end_index - 1

    elif partition_style.lower()[0] == "m":
        # Find the median of the first, middle and last elements.
        x = array_to_partition[start_index]
        y = array_to_partition[end_index - 1]
        z = array_to_partition[int(math.floor((end_index+start_index-1)/2))]
        med = int(numpy.median([x,y,z]))

        # Return the index corresponding to the calculated median.
        if med == x:
            return start_index
        elif med == y:
            return end_index - 1
        else:
            return int(math.floor((end_index+start_index-1)/2))

    elif partition_style.lower()[0] == "r":
        return math.floor(random.random() * end_index + 1)

def quick_sort(sort_array, pivot_type='r'):
    """Sorts an array using the quick sort algorithm."""
    comparisons = quick_sort_internal(sort_array, 0, len(sort_array), pivot_type)
    return result(sort_array, comparisons) 

def quick_sort_internal(sort_array, start_index, end_index, pivot_type):
    """
    Sorts an array using the quick sort algorithm between the start index and
    the end index, and tracks the number of comparisons through all levels of
    recursion.
    """
    assert(start_index >= 0 and end_index <= len(sort_array))

    if end_index - start_index <= 1:
        return 0
    pp = partition(sort_array, start_index, end_index, pivot_type)
    s = start_index
    e = end_index
    comparisons = 0

    # Preprocessing to simplify tracking the sorted and unsorted portions
    # of the array that is being sorted.
    if pp != s:
        sort_array[s], sort_array[pp] = sort_array[pp], sort_array[s]

    c = sort_array[s]
    j = s + 1
    i = s + 1

    while j < e:
        comparisons += 1
        if sort_array[j] < c:
            sort_array[j], sort_array[i] = sort_array[i], sort_array[j]
            i += 1
        j += 1
    sort_array[s], sort_array[i - 1] = sort_array[i - 1], sort_array[s]
    comparisons += quick_sort_internal(sort_array, s, i - 1, pivot_type)
    comparisons += quick_sort_internal(sort_array, i, e, pivot_type)
    return comparisons

def quick_sort_file(file_path, pivot_type):
    """
    Sorts an array stored as a newline-delimited file.
    """
    final_result = quick_sort([int(line) for line in open(file_path)], pivot_type)
    print("Array: %r \n Comparisons: %r" % (final_result.array, final_result.comparisons))


class QuickSortTests(unittest.TestCase):
    def setUp(self):
        self.list_of_ints = []
        for i in range(100000):
            next_int = random.randint(0,10000)
            self.list_of_ints.append(next_int)

    def test_quick_sort(self):
        self.assertEqual(sorted(self.list_of_ints), quick_sort(self.list_of_ints))