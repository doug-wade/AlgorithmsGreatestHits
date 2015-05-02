import unittest
import random
import string
import timeit
from .trie import Trie

class TrieTests(unittest.TestCase):
    def setUp(self):
        self.test_emails = [ "douglas.b.wade@example.com", "doug.wade@example.com", "doug@example.com", "d@example.com" ]
        self.not_present_email = "not_found@example.com"

    def test_add_string_and_find(self):
        trie = Trie()
        for test_email in self.test_emails:
            trie.add_string(test_email)
            self.assertTrue(trie.find(test_email))

    def test_find_returns_none_if_not_found(self):
        trie = Trie()
        for test_email in self.test_emails:
            trie.add_string(test_email)
        self.assertFalse(trie.find(self.not_present_email))

    def test_str(self):
        trie = Trie()
        for test_email in self.test_emails:
            trie.add_string(test_email)
            self.assertTrue(test_email in str(trie))
