"""
An implementation of a graph as a dictionary of dictionaries.
"""
import random

class graph:
    def __init__(self, G={}):
        """
        I guess you might want to build the adjacency hash yourself, and then
        use my class for access?  That'd be weird, but it's not hard to let 
        you do it, so why not.
        """
        self._G = G

    def __getitem__(self, node):
        """
        Gets all edges incident to a node.  Returns a dictionary, with keys as
        nodes to which edges and values as the weight of the edge.
        """
        return self._G[node]

    def add_directed_edge(self, node1, node2, edge_weight):
        """
        Adds a directed edge from node1 to node2 with weight node_weight
        """
        if node1 in self._G:
            self._G[node1][node2] = edge_weight
        else:
            self._G[node1] = { node2: edge_weight }

    def add_undirected_edge(self, node1, node2, edge_weight):
        """
        Adds a undirected edge, represented as reciprocal directed edges from
        node1 to node2 and from node2 to node1, both with weight node_weight.
        """
        self.add_directed_edge(node1, node2, edge_weight)
        self.add_directed_edge(node2, node1, edge_weight)

    def get_nodes(self):
        """
        Gets all the nodes from the graph.
        """
        return self._G.keys()

    def get_edge(self, node1, node2):
        """
        Gets an edge from node1 to node2.  Returns the edge's weight.
        """
        return self._G[node1][node2]

    def get_random_node(self):
        """
        Returns a random node from the graph
        """
        return random.choice(list(self._G.keys()))