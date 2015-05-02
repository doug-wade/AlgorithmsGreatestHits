def merge_sort(array):
    """
    An implementation of the merge sort algorithm.  Recursively sorts arrays
    by calling merge sort on halves of the array, then merging by comparing
    the first element of each array, then adding the smaller of the two to a
    the sorted array.
    """
    # Base Cases
    if len(array) == 1 or len(array) == 0:
        return array
    elif len(array) == 2:
        if array[0] > array[1]:
            array[0], array[1] = array[1], array[0]
        return array
    else:
        i, j, sort = 0, 0, []

        # Split the array into 2 equal parts and sort them
        middle = int(len(array)/2)
        left = merge_sort(array[:middle].copy())
        right = merge_sort(array[middle:].copy())

        # Merge the sorted halves
        ll, lr = len(left), len(right)
        while i < ll and j < lr:
                if left[i] <= right[j]:
                    sort.append(left[i]); i += 1
                else: sort.append(right[j]); j += 1

        # Add anything left over
        sort += left[i:]
        sort += right[j:]

        return sort

def merge_sort_from_file(file_path):
    """
    Performs merge sort on a text file that contains an array containing
    a single element per line.
    """
    return merge_sort([int(line) for line in open(file_path)])
