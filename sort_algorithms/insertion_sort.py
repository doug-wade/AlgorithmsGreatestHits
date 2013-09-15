import unittest
import random

l = [1,3,4,2]
#exchange(l, 3, 1)

def exchange(list_to_exchange, x, y):
    print(list_to_exchange, x, y)
    last_val = list_to_exchange[y]
    print("last val: " + str(last_val))
    for i in range(x, y):
        new_val = list_to_exchange[i+1]
        list_to_exchange[i+1] = list_to_exchange[i]
        print(list_to_exchange)
    list_to_exchange[x] = last_val

def insertion_sort(list_to_sort):
    for i in range(1, len(list_to_sort)):
        for j in range(i-1, -1, -1):
            if list_to_sort[i] > list_to_sort[j-1] and list_to_sort[i] < list_to_sort[j]:
                exchange(list_to_sort, j, i)
                break
    return list_to_sort

class InsertionSortTests(unittest.TestCase):

    def setUp(self):
        self.list_of_ints = []
        for i in range(100000):
            next_int = random.randint(0,10000)
            self.list_of_ints.append(next_int)
        f.close()

    def test_insertion_sort(self):
        self.assertEqual(sorted(self.list_of_ints), heapsort(self.list_of_ints))

print(insertion_sort(l))