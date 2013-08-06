from collections import deque

def get_searched_index(graph):
    """
    Returns a dictionary with a key for each node in the graph with a boolean
    initialized to False, to indicate whether they have not yet been searched.
    """
    searched = {}
    for k in graph.keys():
        searched[k] = False
    return searched

def find_connected_portion(graph, seed, searched_index):
    """
    Returns a set of 
    """
    assert(seed in graph.keys() and searched_index[seed] == False)

    queue, connected_portion = deque([seed]), set()
    while len(queue) > 0:
        k = queue.popleft()
        for node in graph[k]:
            if searched_index[node] == False:
                searched_index[node] = True
                queue.append(node)
                connected_portion |= {node}

    return connected_portion

def undirected_graph_connectivity(graph):
    """
    Using breadth-first search, finds all connected portions of a graph.
    Returns a set of frozensets, with each frozenset representing a group
    of points that are directly or indirectly connected.
    """
    sets, searched_index = set(), get_searched_index(graph)
    for k in searched_index.keys():
        if searched_index[k] == False:
            sets |= {frozenset(find_connected_portion(graph, k, searched_index))}

    return sets

def is_connected(graph):
    return len(undirected_graph_connectivity(graph)) < 2

def get_graph_from_file(file_path):
    """
    Returns an adjacency list for a graph represented in text file, where
    each line of the text file has the first element as the node, and each
    subsequent tab-delimited element defines an edge.
    """
    f = open(file_path)
    graph = {}
    for l in f:
        tempArr = l.split(' ')
        tempArr.remove('\n')
        graph[int(tempArr[0])] = [int(x) for x in tempArr[1:len(tempArr)]]
    return graph

# Example uses:
# print(undirected_graph_connectivity(get_graph_from_file('./tinyGraph.txt')))
# print(is_connected(get_graph_from_file('./tinyGraph.txt')))