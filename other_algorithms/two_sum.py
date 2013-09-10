def find_sums(array, min, max):
    count = 0
    for i in range(min,max):
        if has_two_sum(i, array):
            count += 1
    return count

def has_two_sum(int_to_check, array):
    for key in array:
        if (int_to_check - array[key]) in array and array[key] != array[int_to_check - array[key]]:
            return True
    return False

def get_array_from_file(file_location):
    int_dict = {}
    f = open(file_location)
    for line in f:
        int_dict[int(line)] = int(line)
    return int_dict

int_hash = get_array_from_file('./data/algo1-programming_prob-2sum.txt')
print(find_sums(int_hash,-10000,10000))