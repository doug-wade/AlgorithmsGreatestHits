from random import randint
import unittest
from .karatsuba_multiplication import multiply

class KaratsubaMultiplicationTests(unittest.TestCase):
    def setUp(self):
        self.test_int_pairs = [ (randint(-10000, 10000), randint(-10000, 10000)) for _ in range(20) ]

    def test_rand_ints(self):
        for pair in self.test_int_pairs:
            self.assertEqual(multiply(pair[0], pair[1]), pair[0] * pair[1])

    def test_multiply_by_zero(self):
        self.assertEqual(0, multiply(0, 4352))

    def test_multiply_by_one(self):
        self.assertEqual(8532, multiply(1, 85325))

    def test_multiply_even_times_even(self):
        self.assertEqual(1234 * 5678, multiply(1234, 5678))

    def test_multiply_even_times_odd(self):
        self.assertEqual(11 * 111, multiply(11, 111))

    def test_multiply_odd_times_even(self):
        self.assertEqual(111 * 11, multiply(111, 11))

    def test_multiply_odd_times_odd(self):
        self.assertEqual(111 * 111, multiply(111, 111))
