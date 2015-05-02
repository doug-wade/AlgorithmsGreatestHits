import unittest
import random
import os
from .read_file import read_file

class ReadFileTests(unittest.TestCase):
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

    def tearDown(self):
        os.remove(self.int_file_path)
