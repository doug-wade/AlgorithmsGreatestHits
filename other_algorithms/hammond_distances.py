import sys
sys.path.insert(0, '../data_structures')
from unionfind import UnionFind

def toggle_bit(c):
    if c == '0':
        return '1'
    else:
        return '0'

def update_singles(uf, code, count_bits):
    for i in range(count_bits):
        uf.union(code, code[0:i] + toggle_bit(code[i]) + code[i+1:])

def update_doubles(uf, code, count_bits):
    for i in range(count_bits):
        for j in range(i+1, count_bits):
            uf.union(code, code[0:i] + toggle_bit(code[i]) + code[i+1:j] + toggle_bit(code[j]) + code[j+1:])

def hammond_distances(file_path):
    file_stream = open(file_path)
    line_one = file_stream.readline().split(' ')
    count_edges, count_bits = int(line_one[0]), int(line_one[1])
    uf = UnionFind([])
    for i in range(count_edges):
        code = file_stream.readline()
        code = code.replace(' ', '').replace('\n', '')
        uf.add(code)
        update_singles(uf, code, count_bits)
        update_doubles(uf, code, count_bits)
    file_stream.close()
    clusters = set()
    for k in uf._node_titles.keys():
        clusters.add(uf.find(k))
    return len(clusters)