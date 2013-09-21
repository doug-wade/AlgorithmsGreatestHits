def knapsack(file_path):
    with open(file_path) as file_stream:
        i = 0
        for line in file_stream:
            if i == 0:
                knapsack_size = int(line.split(' ')[0])
                items = int(line.split(' ')[1])
                curr_list = [0 for j in range(knapsack_size)]
            else:
                is_used = False
                value = int(line.split(' ')[0])
                weight = int(line.split(' ')[1])
                prev_list = curr_list
                curr_list = []
                for j in range(knapsack_size):
                    if j < weight:
                        curr_list.append(prev_list[j])
                        continue
                    if prev_list[j] > (prev_list[j-weight] + value):
                        curr_list.append(prev_list[j])
                    else:
                        curr_list.append(prev_list[j-weight] + value)
            i += 1
            # print(curr_list)
    return curr_list[knapsack_size-1]