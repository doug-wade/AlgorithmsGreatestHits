import sys

def dijkstras(graph, start, end):
    """
    Performs Dijkstra's algorithm for finding a shortest path from the start
    node to the end node on the provided graph.
    """
    A, explored = {start:0}, {start}
    x = start
    while x != end:
        minDist, nextNode = sys.maxsize, None
        for n in explored:
            if n not in graph:
                continue
            arcs = (set(graph[n].keys()) - explored)
            for arc in arcs:
                if graph[n][arc] + A[n] < minDist:
                    minDist = graph[n][arc] + A[n]
                    nextNode = arc
        explored |= {nextNode}
        A[nextNode] = minDist
        x = nextNode
    return A

def get_graph_from_file(file_path):
    """
    Returns a directed, weighted graph from a tab-delimited text file, where 
    each line of the text file defines a node (labelled in the first element)
    then a set of tuples, each one containing the node to which an arc points
    from that rows node, and the length/weight of that arc.
    """
    f = open(file_path)
    graph = {}
    for l in f:
        tempArr = l.rstrip().split('\t')
        k = int(tempArr[0])
        graph[k] = {int(y.split(',')[0]):int(y.split(',')[1]) 
                    for y in tempArr[1:len(tempArr)]}
    return graph

questions = [7,37,59,82,99,115,133,165,188,197]
results = {}
g = get_graph_from_file('./dijkstraData.txt')
for q in questions:
    resDict = dijkstras(g, 1, q)
    results[q] = resDict[q]
for key in results:
    print(str(key) + ' ' + str(results[key]))