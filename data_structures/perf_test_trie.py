import random
import string
import timeit
from .trie import Trie
import unittest

class TriePerfTests(unittest.TestCase):
    def test_trie_perf(self):
        def get_random_email():
            top_level_domains = [".net", ".org", ".com"]
            random_email = "".join(random.choice(string.ascii_lowercase) for _ in range(3, 24))
            random_email += "@"
            random_email += "".join(random.choice(string.ascii_lowercase) for _ in range(3, 8))
            random_email += random.choice(top_level_domains)
            return random_email

        test_emails = [ get_random_email() for _ in range(5000) ] * 2
        trie = Trie()
        def dedupe_emails(emails):
            for email in emails:
                trie.add_string(email)
            return str(trie)
        self.assertTrue(timeit.timeit(lambda: dedupe_emails(test_emails), number=3) < 2)
