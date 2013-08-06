import collections
import math

point = collections.namedtuple('Point', ['x', 'y'])

testArray = [point(1,2), point(3, 4), point(0,3)]

def find_closest_pair(pair_list):
    return {pair_list[0], pair_list[1]}

print(find_closest_pair(testArray))