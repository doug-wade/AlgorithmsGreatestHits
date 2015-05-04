from .hashmap import HashMap
from utils.mock_hash import MockHash
import unittest

class HashMapTests(unittest.TestCase):
    def setUp(self):
        self.key_val_pairs = [ (MockHash(0), "zero"), (MockHash(1), "one"), (MockHash(2), "two"), (MockHash(3), "three") ]
        self.hash_collisions = [ (MockHash(42), "collisionZero"), (MockHash(42), "collisionOne"), (MockHash(42), "collisionTwo") ]

    def test_mock_class(self):
        hash_val = 42

        testHash = MockHash(hash_val)
        self.assertEqual(testHash.hash, hash_val)

    def test_put_and_get(self):
        hashmap = HashMap(8)
        for key_val_pair in self.key_val_pairs:
            hashmap.put(key_val_pair[0], key_val_pair[1])
            self.assertEqual(key_val_pair[1], hashmap.get(key_val_pair[0]))

    def test_clear(self):
        hashmap = HashMap(8)
        hashmap.putAll(self.key_val_pairs)
        hashmap.clear()
        for key_val_pair in self.key_val_pairs:
            self.assertEqual(None, hashmap.get(key_val_pair[0]))

    def test_collisions(self):
        hashmap = HashMap(8)
        for key_val_pair in self.hash_collisions:
            hashmap.put(key_val_pair[0], key_val_pair[1])
            self.assertEqual(hashmap.get(key_val_pair[0]), key_val_pair[1])

    def test_keys(self):
        hashmap = HashMap(8)
        hashmap.putAll(self.key_val_pairs)
        hashmap.putAll(self.hash_collisions)
        for key_val_pair in self.hash_collisions:
            self.assertTrue(key_val_pair[0] in hashmap.keys())
        for key_val_pair in self.key_val_pairs:
            self.assertTrue(key_val_pair[0] in hashmap.keys())
