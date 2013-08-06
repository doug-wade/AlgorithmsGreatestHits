import random
import math

def choose_random_edge(g):
    """Chooses a random edge, as defined by a pair of nodes."""
    randKey1 = random.choice(list(g.keys()))
    randKey2 = random.choice(g[randKey1])
    return randKey1, randKey2

def random_contraction(graph_to_contract):
    """Performs a random contraction on a graph."""
    gtc = graph_to_contract.copy()
    while len(gtc) > 2:
        rk1, rk2 = choose_random_edge(gtc)
        # change all of the instance of node 2 to node 1
        for l in gtc:
            gtc[l] = [rk1 if x == rk2 else x for x in gtc[l]]
        # all edges from node 2 are now edges from node 1
        gtc[rk1].extend(gtc[rk2])
        # remove self loops
        while rk1 in gtc[rk1]:
            gtc[rk1].remove(rk1)
        # remove node 2
        del gtc[rk2]
    # both should be the same length, so either will work.
    return len(gtc[random.choice(list(gtc.keys()))])

def karger_contraction(graph):
    """Finds a minimum contraction with 99%% accuracy"""
    count_nodes = len(graph.keys())
    num_iter = math.floor((count_nodes**2) * math.log(count_nodes))
    cuts = count_nodes
    for i in range(num_iter):
        new_cuts = random_contraction(graph)
        if new_cuts < cuts:
            cuts = new_cuts
    return cuts

def get_graph_from_file(file_path):
    """
    Returns an adjacency list for a graph represented in text file, where
    each line of the text file has the first element as the node, and each
    subsequent tab-delimited element defines an edge.
    """
    f = open(file_path)
    graph = {}
    for l in f:
        tempArr = l.split('\t')
        tempArr.remove('\n')
        graph[int(tempArr[0])] = [int(x) for x in tempArr[1:len(tempArr)]]
    return graph

print(karger_contraction(get_graph_from_file('kargerMinCut.txt')))