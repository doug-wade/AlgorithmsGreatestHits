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

    def add(self, val, parent=None):
        """
        Adds a new value, val, to the union find as a member of the cluster
        cluster. If no cluster is provided, val is added to its own cluster.
        """
        node_val = len(self._node_array)
        self._node_titles[val] = node_val
        if parent == None:
            parent = node_val
        else:
            parent = self._node_titles[parent]
        self._node_array.append(self.Node(val, parent, 0))

    def union(self, x, y):
        """
        Unions the regions containing x and y.
        """
        if x not in self._node_titles or y not in self._node_titles:
            return
        x_parent_index = self._find(self._node_titles[x])
        x_parent = self._node_array[x_parent_index]
        y_parent_index = self._find(self._node_titles[y])
        y_parent = self._node_array[y_parent_index]
        if x_parent == y_parent:
            return
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
        if node_to_find not in self._node_titles:
            return
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
