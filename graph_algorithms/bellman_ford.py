def bellman_ford(g):
    pass

def load_graph_from_file(file_path):
    g = graph()
    with open(file_path) as file_stream:
        l1 = file_stream.readline().split(' ')
        count_nodes, count_edges = int(l1[0]), int(l1[1])
        for line in file_stream:
            e = line.split(' ')
            g.add_directed_edge(int(e[0]), int(e[1]), int(e[2]))
    return g

testg = load_graph_from_file('../data/tinyGraph.txt')
print(bellman_ford(testg))