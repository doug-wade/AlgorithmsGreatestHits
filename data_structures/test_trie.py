import unittest
import random
import re
from .trie import Trie

class TrieTests(unittest.TestCase):
    def setUp(self):
        self.test_emails = [ "douglas.b.wade@example.com", "doug.wade@example.com", "doug@example.com", "d@example.com" ]
        self.not_present_email = "not_found@example.com"
        self.vowel_pattern = re.compile("[aeiouAEIOU]")
        self.any_letter_pattern = re.compile("[a-zA-Z]")

        self.under_test = Trie()
        for test_email in self.test_emails:
            self.under_test.add_string(test_email)

    def test_add_string_and_find(self):
        for test_email in self.test_emails:
            self.assertEqual(self.under_test.find(test_email), test_email)

    def test_find_returns_none_if_not_found(self):
        self.assertEqual(self.under_test.find(self.not_present_email), "")

    def test_str(self):
        under_test_str = str(self.under_test)
        for test_email in self.test_emails:
            self.assertTrue(test_email in under_test_str)

    def test_find_prefix(self):
        for test_email in self.test_emails:
            self.assertEqual(self.under_test.find(test_email.split("@")[0]), "")

    def test_fuzzy_find_exact_match(self):
        for test_email in self.test_emails:
            self.assertEqual([ test_email ], self.under_test.fuzzy_find(test_email))

    def test_fuzzy_find_wrong_case(self):
        for test_email in self.test_emails:
            self.assertEqual([ test_email ], self.under_test.fuzzy_find(test_email.upper()))

    def test_fuzzy_find_wrong_vowel(self):
        def get_random_vowel(_):
            return random.choice("aeiou")
        for test_email in self.test_emails:
            to_fuzzy_find = self.vowel_pattern.sub(get_random_vowel, test_email)
            self.assertEqual([ test_email ], self.under_test.fuzzy_find(to_fuzzy_find))

    def test_fuzzy_find_returns_no_suggestion_if_not_found(self):
        self.assertEqual([ "NO SUGGESTION"], self.under_test.fuzzy_find(self.not_present_email))

    def test_fuzzy_find_with_repeated_letters(self):
        def double_letter(match):
            return match.group(0) * 2
        for test_email in self.test_emails:
            to_fuzzy_find = self.any_letter_pattern.sub(double_letter, test_email)
            print(to_fuzzy_find)
            self.assertEqual([ test_email ], self.under_test.fuzzy_find(to_fuzzy_find))
