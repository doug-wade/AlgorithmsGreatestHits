import random
import unittest

def find_min(start, array_to_search):
    """
    Finds the index of the minimum value in a list after position at the start.
    """
    curr_min_index, curr_min_value = float('Infinity'), float('Infinity')
    for i in range(start, len(array_to_search)):
        if array_to_search[i] < curr_min_value:
            curr_min_index = i
            curr_min_value = array_to_search[i]
    return curr_min_index

def selection_sort(comparable_array):
    """
    Performs selection sort.
    """
    for i in range(len(comparable_array)):
        min_index = find_min(i, comparable_array)
        comparable_array[i], comparable_array[min_index] = comparable_array[min_index], comparable_array[i]
    return comparable_array

class selection_sort_tests(unittest.TestCase):
    def setUp(self):
        self.list_of_ints = []
        for i in range(5000):
            next_int = random.randint(0,10000)
            self.list_of_ints.append(next_int)

    def test_find_min(self):
        self.assertEqual(min(self.list_of_ints), self.list_of_ints[find_min(0, self.list_of_ints)])

    def test_selection_sort(self):
        self.assertEqual(sorted(self.list_of_ints), selection_sort(self.list_of_ints))