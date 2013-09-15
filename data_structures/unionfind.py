import unittest

class UnionFind:
    """
    A Union-Find implementation with lazy unions, union-by-rank, and path 
    compression for nodes with arbitrary labels.
    """
    def __init__(self, starting_nodes):
        """
        Takes a list, starting_nodes, of the labels of the nodes and creates a
        UnionFind with each node as its own root.
        """
        self._node_array = []
        self._node_titles = {}
        for i in range(len(starting_nodes)):
            self._node_array.append(self.Node(starting_nodes[i], i, 0))
            self._node_titles[starting_nodes[i]] = i

    class Node:
        """
        The inner class for a single node in the UnionFind.
        """
        def __init__(self, label, parent, rank=0):
            """
            Initializes a node with parent parent and rank rank.
            """
            self._label = label
            self._parent = parent
            self._rank = rank

    def union(self, x, y):
        """
        Unions the regions containing x and y.
        """
        x_parent_index = self._find(self._node_titles[x])
        x_parent = self._node_array[x_parent_index]
        y_parent_index = self._find(self._node_titles[y])
        y_parent = self._node_array[y_parent_index]
        if x_parent._rank > y_parent._rank:
            y_parent._parent = x_parent_index
        elif x_parent._rank > y_parent._rank:
            x_parent._parent = y_parent_index
        else:
            x_parent._parent = y_parent_index
            x_parent._rank += 1

    def find(self, node_to_find):
        """
        Returns the leader for the group that node_to_find is in. Also performs
        path compression.
        """
        position = self._node_titles[node_to_find]
        parent = self._node_array[self._find(position)]
        return parent._label

    def _find(self, loc):
        """
        The internal find method that uses the position of nodes in the array
        instead of node labels to simplify and speed up recursion.
        """
        if self._node_array[loc]._parent == loc:
            return loc
        else:
            new_parent = self._find(self._node_array[loc]._parent)
            self._node_array[loc]._parent = new_parent
            return new_parent

    def size(self):
        """
        Gets the number of nodes in the UnionFind
        """
        return len(self._node_array)

class UnionFindTests(unittest.TestCase):
    def setUp(self):
        self.nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.U = UnionFind(self.nodes)

    def test_find_pre_union(self):
        self.assertEqual(self.U.find('a'), 'a')

    def test_single_union(self):
        self.U.union('a', 'b')
        self.assertEqual(self.U.find('a'), 'b')

    def test_multi_union(self):
        self.U.union('a', 'b')
        self.U.union('c', 'd')
        self.U.union('a', 'd')
        self.U.union('e', 'f')
        self.U.union('g', 'h')
        self.U.union('f', 'h')
        self.U.union('c', 'g')
        #should be fully connected
        leader = None
        for node in self.nodes:
            if leader:
                self.assertEqual(leader, self.U.find(node))
            else:
                leader = self.U.find(node)

    def test_path_compression(self):
        self.U.union('a', 'b')
        self.U.union('c', 'd')
        self.U.union('a', 'd')
        self.U.union('e', 'f')
        self.U.union('g', 'h')
        self.U.union('f', 'h')
        self.U.union('c', 'g')
        #Currently, 'a' is a leaf
        self.assertEqual(self.U._node_array[0]._parent, 1)
        self.U.find('a')
        #Now, 'a' should be directly attached to its leader, as should b.
        self.assertEqual(self.U._node_array[0]._parent, 7)
        self.assertEqual(self.U._node_array[1]._parent, 7)
