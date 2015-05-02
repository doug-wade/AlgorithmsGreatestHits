def exchange(list_to_exchange, x, y):
    last_val = list_to_exchange[y]
    for i in range(y, x, -1):
        list_to_exchange[i] = list_to_exchange[i-1]
    list_to_exchange[x] = last_val

def insertion_sort(list_to_sort):
    for i in range(1, len(list_to_sort)):
        if list_to_sort[i] > list_to_sort[i-1]:
            #Already in the correct place; no need to loop
            continue

        for j in range(i-1, -1, -1):
            if j == 0:
                if list_to_sort[i] < list_to_sort[0]:
                    exchange(list_to_sort, 0, i)
                else:
                    exchange(list_to_sort, 1, i)
            elif list_to_sort[i] > list_to_sort[j-1] and list_to_sort[i] <= list_to_sort[j]:
                exchange(list_to_sort, j, i)
                break
    return list_to_sort
