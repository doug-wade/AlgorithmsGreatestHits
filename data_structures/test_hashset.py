from .hashset import HashSet
from utils.mock_hash import MockHash
import unittest

class HashSetTests(unittest.TestCase):
    def setUp(self):
        self.set_elements = [MockHash(1), MockHash(2), MockHash(3), MockHash(4), MockHash(3, 1), MockHash(4, 2)]
        self.not_contained = MockHash(5)

    def test_add_and_contains(self):
        under_test = HashSet()
        for elem in self.set_elements:
            under_test.add(elem)

        for elem in self.set_elements:
            self.assertTrue(under_test.contains(elem))

    def test_addall_and_size(self):
        under_test = HashSet()
        under_test.add_all(self.set_elements)
        self.assertEqual(len(self.set_elements), under_test.size())

    def test_add_duplicates(self):
        under_test = HashSet()
        test_string = "derp"
        for _ in range(100):
            under_test.add(test_string)
        self.assertEqual(1, under_test.size())
        self.assertTrue(under_test.contains(test_string))

    def test_add_all_duplicates(self):
        under_test = HashSet()
        test_int = 4
        under_test.add_all([ test_int for _ in range(10) ])
        under_test.add_all([ test_int for _ in range(10) ])

        self.assertEqual(1, under_test.size())
        self.assertTrue(under_test.contains(test_int))

    def test_contains_with_missing_element(self):
        under_test = HashSet()
        under_test.add_all(self.set_elements)

        self.assertFalse(under_test.contains(self.not_contained))
