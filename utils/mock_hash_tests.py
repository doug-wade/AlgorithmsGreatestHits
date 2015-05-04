import unittest
from .mock_hash import MockHash

class MockHashTest(unittest.TestCase):
    def setUp(self):
        self.hash_val = 42
        self.underTest = MockHash(self.hash_val)
        self.collision = MockHash(self.hash_val, self.hash_val + 1)

    def test_hash(self):
        self.assertEqual(self.underTest.hash, self.hash_val)

    def test_hash_collision(self):
        self.assertTrue(self.underTest.hash == self.collision.hash)
        self.assertFalse(self.underTest == self.collision)
