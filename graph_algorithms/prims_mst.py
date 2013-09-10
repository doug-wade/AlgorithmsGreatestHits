import os
import pdb
from heaps import tuple_min_heapq
from graph import graph

def update_node_heap(graph, node_heap, added_node, explored):
    """
    Maintains the node heap invariant by ensuring that the key for a node is
    always the shortest edge from the explored area.
    """
    for key in graph[added_node]:
        # print(str(key) + " " + str(explored.keys()))
        if key in explored.keys():
            # print("(explored)")
            node_heap.delete(key)
        else:
            if not node_heap.contains(key):
                # print("(adding " + str(key) + " with weight " + str(graph[added_node][key]) + ")")
                node_heap.push(key, graph[added_node][key])
            elif node_heap[key] > graph[added_node][key]:
                # print("(changing from " + str(node_heap[key]) + " to " + str(graph[added_node][key]))
                node_heap.update(key, graph[added_node][key])

def prims_mst(graph):
    """
    Performs Prim's Minimum Spanning Tree algorithm on a custom graph class.
    """
    S = graph.get_random_node()
    # print("Starting with " + str(S))
    X = { S:True }
    node_heap = tuple_min_heapq()
    total_weight = 0

    while X.keys() != graph.get_nodes():
        update_node_heap(graph, node_heap, S, X)
        # pdb.set_trace()
        S, weight = node_heap.pop()
        # print(str(S) + ": " + str(weight))
        total_weight += weight
        X[S] = True

    return total_weight

def get_graph_from_file(file_path):
    """
    Returns an undirected graph from a file, stored with the first line as the
    number of edges and nodes (respectively), with each line thereafter 
    representing an edge between two nodes (the first two numbers delimited by
    spaces) with a weight, represented by the third space-delimited number.
    """
    file_graph = graph()

    file_stream = open(file_path)
    line = file_stream.readline().split(" ")
    num_nodes, num_edges = int(line[0]), int(line[1])

    for i in range(num_edges):
        line = file_stream.readline().split(" ")
        file_graph.add_undirected_edge(int(line[0]), int(line[1]), int(line[2]))

    return file_graph

# print(get_graph_from_file("./data/edges.txt"))
adj_list = get_graph_from_file("./data/tinyGraph.txt")

# inspect the graph:
# for node in adj_list.get_nodes():
#     print(str(node) + ": " + str(adj_list.get_node(node)))

print(prims_mst(adj_list))