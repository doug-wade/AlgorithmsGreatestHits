from collections import deque

def depth_first_search(graph, start, path, explored):
    """
    Performs depth-first search to find a sink node.  At the sink node, it
    appends the sink node to a queue, which tracks the topological sorting
    of the graph.
    """
    explored |= {start}
    if start in graph.keys():
        for x in graph[start]:
            if x not in explored:
                depth_first_search(graph, x, path, explored)
    path.appendleft(start)

def topological_sort(graph):
    """
    Performs a topological sort on a directed graph.  Returns an appropriately
    sorted queue.
    """
    explored = set()
    path = deque()
    for key in graph.keys():
        if key not in explored:
            depth_first_search(graph, key, path, explored)
    return path

def get_graph_from_file(file_path, isReversed=False):
    """
    Returns an adjacency list for a graph represented in text file, where
    each line of the text file defines an arc, pointing from the first 
    element to the second element (delimited by a space).
    """
    f = open(file_path)
    if isReversed == False:
        i,j = 0,1
    else:
        i,j = 1,0
    graph = {}
    for l in f:
        tempArr = l.rstrip().split(' ')
        k = tempArr[i]
        v = tempArr[j]
        if k in graph:
            graph[k].append(v)
        else:
            graph[k] = [v]
    return graph

print(topological_sort(get_graph_from_file('./tinySCC.txt')))