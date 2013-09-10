import math
import unittest
import random

def karatsuba_multiply(int1, int2):
    """
    An implementation of the Karatsuba algorithm for integer multiplication.
    Returns the equivalent of int1 * int2.
    """
    # Base case
    if int1 < 10 or int2 < 10:
        return int1 * int2

    # Set up
    strInt1 = str(int1)
    strInt2 = str(int2)
    len1 = len(strInt1)
    len2 = len(strInt2)
    mid1 = math.ceil(len1/2)
    mid2 = math.ceil(len2/2)
    m = max(len1, len2)

    # Get primitives
    lhs1 = int(strInt1[:mid1])
    rhs1 = int(strInt1[mid1:])
    lhs2 = int(strInt2[:mid2])
    rhs2 = int(strInt2[mid2:])

    # Get components
    n1 = karatsuba_multiply(lhs1, lhs2)
    n2 = karatsuba_multiply(rhs1, rhs2)
    n3 = karatsuba_multiply((lhs1+rhs1), (lhs2+rhs2))

    if m % 2:
        return (n1 * 10**(m - math.floor(m/2))) + ((n3 - n2 - n1) * 10**math.floor(m/2)) + n2
    else:
        return (n1 * 10**m) + int((n3 - n2 - n1) * 10**(m/2)) + n2

class karatsubaTests(unittest.TestCase):
    def test_karatsuba_multiply(self):
        for i in range(1000):
            int1 = random.randint(0,10000)
            int2 = random.randint(0,10000)
            self.assertEqual(int1 * int2, karatsuba_multiply(int1, int2))