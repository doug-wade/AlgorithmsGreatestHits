from ..data_structures import Graph

def floyd_warshall(g):
    n = len(g.get_nodes())
    currA = []
    for i in range(n+1):
        currA.append([])
        for j in range(n+1):
            if g.get_edge(i,j) != None:
                currA[i].append(g.get_edge(i,j))
            else:
                currA[i].append(float("inf"))
    for k in range(1, n+1):
        prevA = currA
        for i in range(1, n+1):
            for j in range(1, n+1):
                c1 = prevA[i][j]
                c2 = prevA[i][k] + prevA[k][j]
                if c1 < c2:
                    currA[i][j] = c1
                else:
                    currA[i][j] = c2
    for i in range(1, n+1):
        if currA[i][i] < 0:
            return None
    return currA

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
# g1 = load_graph_from_file('../data/g1.txt')
# g2 = load_graph_from_file('../data/g2.txt')
# g3 = load_graph_from_file('../data/g3.txt')
print(floyd_warshall(testg))