from collections import deque

def get_searched_index(graph, start, nodes_count):
    """
    Returns a dictionary with a key for each node in the graph with an integer
    initialized to the total number of nodes, which is more than the maximum
    number of levels, since we're counting levels from 0, so it can double as
    a bool indicating whether the node has been searched.
    """
    searched = {}
    for k in graph.keys():
        if k == start:
            searched[k] = 0
        else:
            searched[k] = nodes_count
    return searched

def traceback_path(searched_index, start, goal):
    """
    Walks a search index backwards from the end to the start, then returns a
    stack representing a shortest path from start to goal.
    """
    path = []
    curr_step = goal

    while curr_step != start:
        path.append(curr_step)
        curr_step = searched_index[curr_step]

    path.append(curr_step)
    return path

def get_shortest_path(graph, start, goal):
    """
    Finds a shortest path from the start to the goal by moving along undirected
    edges of the provided graph.
    """
    assert(start in graph.keys() and goal in graph.keys())

    # The Set-Up (You Need This) -- doo doo doo doo doo doo doo doo doo doo doo
    nodes_count = len(graph.keys())
    searched_index = get_searched_index(graph, start, nodes_count)
    queue = deque([start])

    while len(queue) > 0:
        k = queue.popleft()
        for node in graph[k]:
            if searched_index[node] != nodes_count:
                continue
            print(node)
            searched_index[node] = k
            if node == goal:
                return traceback_path(searched_index, start, goal)
            if searched_index[node] != nodes_count:
                queue.append(node)

    # There is no path
    return []

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
        graph[tempArr[0]] = [x for x in tempArr[1:len(tempArr)]]
    return graph

# Example uses:
print(get_shortest_path(get_graph_from_file('./tinyGraph.txt'), 'b', 'd'))