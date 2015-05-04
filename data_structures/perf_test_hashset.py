import random
import string
import timeit
from data_structures.hashset import HashSet
import unittest

class HashSetTests(unittest.TestCase):
    def test_perf(self):
        def get_random_email():
            top_level_domains = [ ".net", ".org", ".com" ]
            random_email = "".join(random.choice(string.ascii_lowercase) for _ in range(random.randint(3, 24)))
            random_email += "@"
            random_email += "".join(random.choice(string.ascii_lowercase) for _ in range(random.randint(3, 8)))
            random_email += random.choice(top_level_domains)
            return random_email

        test_emails = [ get_random_email() for _ in range(50000) ] * 2
        random.shuffle(test_emails)
        def dedupe_emails(emails):
            encountered = HashSet()
            deduped = []
            for email in emails:
                if not encountered.contains(email):
                    deduped.append(email)
                    encountered.add(email)
            return deduped
        self.assertTrue(timeit.timeit(lambda: dedupe_emails(test_emails), number=1) < 1)
