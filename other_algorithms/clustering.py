import sys
sys.path.insert(0, '../data_structures')
from unionfind import UnionFind

def clustering(edge_list, count_nodes, clusters):
    u = UnionFind([x+1 for x in range(count_nodes)])
    count_edges = len(edge_list)
    i = 0
    while True:
        if not u.find(edge_list[i][1][0]) == u.find(edge_list[i][1][1]):
            if count_nodes <= clusters:
                return edge_list[i][0], u
            u.union(edge_list[i][1][0], edge_list[i][1][1])
            count_nodes -= 1
        i += 1

def preprocess(file_path):
    edge_list = []
    with open(file_path) as file_stream:
        count_nodes = int(file_stream.readline())
        for line in file_stream:
            edge = line.split(' ')
            edge_list.append((int(edge[2]), (int(edge[0]), int(edge[1]))))
    return sorted(edge_list), count_nodes

def do_clustering(file_path):
    el, cn = preprocess(file_path)
    w, uf = clustering(el, cn, 4)
    return w