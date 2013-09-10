import sys
sys.path.insert(0, '../data_structures')

from heaps import minheapq, maxheapq
import unittest
import random
import os

def heapsort(int_list, max_first=False):
    """
    An implementation of heap sort.
    """
    if max_first:
        heap = maxheapq()
    else:
        heap = minheapq()
    for integer in int_list:
        heap.push(integer)
    for i in range(len(int_list)):
        int_list[i] = heap.pop()
    return int_list


def read_file(file_path):
    """
    Reads an array of integers from a file where they are stored one per line.
    """
    file_stream = open(file_path, 'r')
    int_list = []
    for line in file_stream:
        int_list.append(int(line))
    file_stream.close()
    return int_list

class HeapSortTests(unittest.TestCase):

    def setUp(self):
        self.int_file_path = './temp_int_file.txt'
        self.list_of_ints = []
        f = open(self.int_file_path, 'w')
        for i in range(100000):
            next_int = random.randint(0,10000)
            self.list_of_ints.append(next_int)
            f.write(str(next_int) + '\n')
        f.close()

    def test_read_from_file(self):
        self.assertEqual(self.list_of_ints, read_file(self.int_file_path))

    def test_heapsort(self):
        self.assertEqual(sorted(self.list_of_ints), heapsort(self.list_of_ints))

    def test_heapsort_reverse(self):
        self.assertEqual(sorted(self.list_of_ints, reverse=True), 
            heapsort(self.list_of_ints, True))

    def tearDown(self):
        os.remove(self.int_file_path)

if __name__ == '__main__':
    unittest()