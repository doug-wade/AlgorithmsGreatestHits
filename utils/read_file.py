def read_file(file_path):
    """
    Reads an array of integers from a file where they are stored one per line.
    """
    file_stream = open(file_path, 'r')
    int_list = []
    for line in file_stream:
        int_list.append(int(line))
    file_stream.close()
    return int_list
