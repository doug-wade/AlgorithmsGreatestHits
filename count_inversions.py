import os
import math
import collections

# ./IntegerArray.txt is the real deal; this file is for debugging 
array_location = './tinyArray.txt'

# An object to pass around the results
sorted_result = collections.namedtuple('sorted_result', ['inversions','array'])

# Does the actual inversion counting while merging the two halves
def merge_arrays(left_hand_side, right_hand_side, inversions_count):
    sorted_array = []
    i = 0
    j = 0
    lhs_len = len(left_hand_side)
    rhs_len = len(right_hand_side)
    while True:
        # We've fallen off one of the arrays, so append the rest of the result
        # onto the sorted array. All inversions have already been counted in the if/else below.
        if i >= lhs_len:
            sorted_array.extend(right_hand_side[j:])
            return sorted_result(inversions_count, sorted_array)
        if j >= rhs_len:
            sorted_array.extend(left_hand_side[i:])
            return sorted_result(inversions_count, sorted_array)
        # The ideal case is to copy everything from the left_hand_side, 
        # then from the right_hand_side. Any deviation from that pattern
        # implies len(right_hand_side) inversions.
        if left_hand_side[i] < right_hand_side[j]:
            sorted_array.append(left_hand_side[i])
            i+=1
        else:
            sorted_array.append(right_hand_side[j])
            j+=1
            inversions_count += len(left_hand_side[i:])

# Handles splitting, recursing, and base cases.  
# Can be used as an entry point if the array is a local variable.
def count_array_inversions(array, inversions_count):
    array_len = len(array)
    if array_len < 2:
        return sorted_result(inversions_count, array)
    split_location = math.floor(array_len/2)
    left_result = count_array_inversions(
        array[:split_location], inversions_count)
    right_result = count_array_inversions(
        array[split_location:], inversions_count)
    return merge_arrays(left_result.array, right_result.array,
        left_result.inversions + right_result.inversions)

# The entry point if the array is a newline-delimited file.
def count_file_inversions(file_path):
    final_result = count_array_inversions(
        [int(line) for line in open(file_path)], 0)
    print("There were %d inversions." % final_result.inversions)

# The homework script.
count_file_inversions(array_location)