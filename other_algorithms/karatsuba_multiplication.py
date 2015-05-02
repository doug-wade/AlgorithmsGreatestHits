import math

def multiply(int1, int2):
    """
    An implementation of the Karatsuba algorithm for integer multiplication.
    Returns product of int1 and int2.
    """
    # Base case
    if (int1 < 10 and int1 > -10) or (int2 < 10 and int2 > -10):
        return int1 * int2

    # Set up
    strInt1 = str(int1)
    strInt2 = str(int2)
    len1 = len(strInt1)
    len2 = len(strInt2)
    mid1 = math.floor(len1/2)
    mid2 = math.floor(len2/2)
    m = max(len1, len2)
    m2 = math.floor(m/2)

    # Get primitives
    lhs1 = int(strInt1[:mid1])
    rhs1 = int(strInt1[mid1:])
    lhs2 = int(strInt2[:mid2])
    rhs2 = int(strInt2[mid2:])

    # Get components
    n0 = multiply(lhs1, lhs2)
    n1 = multiply(lhs1 + rhs1, lhs2 + rhs2)
    n2 = multiply(rhs1, rhs2)

    return (n2 * (10**(2*m2))) + ((n1 - n2 - n0) * 10**(m2)) + n0
