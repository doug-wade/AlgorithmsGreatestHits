from heaps import maxheapq, minheapq

def sum_medians(medians):
    """
    Takes a list of integers; returns a sum of all elements.
    """
    sum_of_medians = 0
    for m in medians:
        sum_of_medians += m
    return sum_of_medians

def median_maintenance(file_location):
    """
    Keeps track of the median at all times in a stream of integers.
    """
    bottom_half, top_half, medians = maxheapq(), minheapq(), []
    max_bottom, min_top, count_ints = 0, 0, 0

    f = open(file_location)
    for line in f:
        new_int = int(line)

        # Don't let the initialization values get in the stream.
        if count_ints < 2:
            if count_ints < 1:
                medians.append(new_int)
                min_top = new_int
                count_ints += 1
            else:
                count_ints += 1
                if new_int > min_top:
                    max_bottom = min_top
                    min_top = new_int
                else:
                    max_bottom = new_int
                medians.append(max_bottom)
            continue

        # Put the new int in the right place
        if new_int > min_top:
            top_half.push(new_int)
        elif new_int < max_bottom:
            bottom_half.push(new_int)
        # The new int is a/the new median; correct imbalances if possible
        elif top_half.length() > bottom_half.length():
            bottom_half.push(max_bottom) # new_int is greater than max_bottom
            max_bottom = new_int
        else:
            top_half.push(min_top)
            min_top = new_int
        
        # Rebalance the heaps
        if bottom_half.length() > top_half.length() + 1:
            top_half.push(min_top)
            min_top = max_bottom
            max_bottom = bottom_half.pop()
        elif top_half.length() > bottom_half.length() + 1:
            bottom_half.push(max_bottom)
            max_bottom = min_top
            min_top = top_half.pop()

        # Get the new median and add it to the median list
        if (bottom_half.length() + top_half.length()) % 2:
            if bottom_half.length() > top_half.length():
                medians.append(max_bottom)
            else:
                medians.append(min_top)
        else:
            medians.append(max_bottom)

    return(sum_medians(medians))
