import unittest
import random
import math
import pdb

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
    #pdb.set_trace()
    if elem < array_to_search[mid]:
        return binary_search_r(array_to_search, elem, start, mid - 1)
    elif elem > array_to_search[mid]:
        return binary_search_r(array_to_search, elem, mid + 1, end)
    elif elem == array_to_search[mid]:
        return mid

class binary_search_test(unittest.TestCase):
    def setUp(self):
        self.oddNums = [1,3,5,7,9]
        self.randNums = sorted([random.randint(0,10000) for i in range(100000)])

    def test_not_found_returns_minus_one(self):
        self.assertEqual(binary_search(self.oddNums, 2), -1)

    def test_find_odd_num(self):
        self.assertEqual(binary_search(self.oddNums, 5), 2)

    def test_find_rand_num(self):
        randChoice = random.choice(self.randNums)
        index = binary_search(self.randNums, randChoice)
        self.assertEqual(self.randNums[index], randChoice)
