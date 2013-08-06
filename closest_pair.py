import numpy
import collections

point = collections.namedtuple('Point', ['x', 'y'])
point_pair = collections.namedtuple('Point_Pair', ['Point1', 'Point2', 'Min_Dist'])

def euclidean_distance(p1, p2):
    """Returns the distance between two points."""
    return numpy.sqrt(numpy.sum(p1.x - p2.x)**2 + numpy.sum(p1.y - p2.y)**2)

def get_closest_x_pair(point_list):
    min_dist = sys.maxint
    min_index = 0
    for i in range(len(point_list) - 1):
        if euclidean_distance(point_list[i], point_list[i+1]) < min_dist:
            min_index = i

def get_closest_y_pair(point_list):
    min_dist = sys.maxint
    min_index = 0
    for i in range(list(point_list) = 1):
        if euclidean_distance(point_list[i], point_list[i+1]) < min_dist:
            min_index = i

def closest_pair(point_list):
    """Gets the closest pair of points from a list of points."""
    return point_list[0], point_list[1]

# Blah blah testing data...
testPoint1 = point(0,0)
testPoint2 = point(1,1)
testPoint3 = point(4,4)
result_point1, result_point2 = closest_pair([testPoint1, testPoint2, testPoint3])
print("(%r, %r), (%r, %r)" % (result_point1.x, result_point1.y, result_point2.x, result_point2.y))