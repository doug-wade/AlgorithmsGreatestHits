def find_min(start, array_to_search):
    """
    Finds the index of the minimum value in a list after position at the start.
    """
    curr_min_index, curr_min_value = float('Infinity'), float('Infinity')
    for i in range(start, len(array_to_search)):
        if array_to_search[i] < curr_min_value:
            curr_min_index = i
            curr_min_value = array_to_search[i]
    return curr_min_index

def selection_sort(comparable_array):
    """
    Performs selection sort.
    """
    for i in range(len(comparable_array)):
        min_index = find_min(i, comparable_array)
        comparable_array[i], comparable_array[min_index] = comparable_array[min_index], comparable_array[i]
    return comparable_array
