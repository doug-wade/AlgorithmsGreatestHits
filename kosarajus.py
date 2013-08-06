from collections import deque
from threading import Thread
import sys
import threading

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

def topological_sort_one(graph, sort_order):
    """
    Performs a topological sort on a directed graph.  Returns an appropriately
    sorted queue.
    """
    path, explored = deque(), set()
    for key in sort_order:
        if key not in explored:
            depth_first_search(graph, key, path, explored)
    return path

def topological_sort_two(graph, sort_order):
    """
    Performs a topological sort on a directed graph, while tracking boundaries
    between strongly sorted components.  Returns a list of sets, each 
    representing a strongly connected components.
    """
    path, boundaries, explored = deque(), deque(), set()
    for key in sort_order:
        if key not in explored:
            boundaries.appendleft(key)
            depth_first_search(graph, key, path, explored)
    b = boundaries.pop()
    scc = set()
    sccs = []
    while len(path):
        elem = path.pop()
        scc |= {elem}
        if elem == b:
            if len(boundaries):
                b = boundaries.pop()
            else:
                scc |= set(path)
                sccs.append(scc)
                return sccs
            sccs.append(scc.copy())
            scc.clear()

def kosarajus_two_pass_algorithm(file_path):
    """
    Uses Kosaraju's Two Pass algorithm to identify strongly connected 
    components in a directed graph.  Uses a file for data storage for
    simpler memory management.
    """
    rev_graph = get_graph_from_file(file_path, True)
    finishing = topological_sort_one(rev_graph, deque(rev_graph.keys()))

    # Loading the graph from file twice does indeed double the load time, as
    # expected, but on my benchmarking on a directed graph of 5.1 million arcs, 
    # w/something something 8GB RAM something something hardware, it only 
    # requires an extra ~7.4 seconds, much less than the total running time of
    # the full algorithm.
    del rev_graph
    graph = get_graph_from_file(file_path, False)
    return topological_sort_two(graph, finishing)


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

def process_sccs(l):
    lens = []
    for t in l:
        lens.append(len(t))
    lens.sort()
    return lens

class MyThread(Thread):
    def run(self):
        print(process_sccs(kosarajus_two_pass_algorithm('./SCC.txt')))
