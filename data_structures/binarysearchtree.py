class BinarySearchTree:
    """
    The most simple version of a binary search tree, implemented as a recursive
    data structure.
    """
    def __init__(self):
        """
        Initializes an empty binary search tree.
        """
        self._root = None

    class Node:
        """
        Represents a node in the binary search tree.
        """
        def __init__(self, value, rank=1, left=None, right=None):
            self._value = value
            self._left = left
            self._right = right
            self._rank = rank

        def _rerank(self):
            """
            Updates _rank to match the rank of it's children.
            """
            if self._left:
                lr = self._left._rank
            else:
                lr = 0
            if self._right:
                rr = self._right._rank
            else:
                rr = 0
            self._rank = lr + rr + 1

    def add(self, value):
        """
        Adds a new node to the binary search tree.
        """
        if self._root == None:
            self._root = self.Node(value)
        else:
            self._add(self._root, value)

    def _add(self, node, value):
        """
        The recursive helper function for add().
        """
        if value < node._value:
            if node._left == None:
                node._left = self.Node(value)
                node._rank += 1
            else:
                self._add(node._left, value)
        elif value > node._value:
            if node._right == None:
                node._right = self.Node(value)
                node._rank += 1
            else:
                self._add(node._right, value)
        # Else is implicit -- if the value is neither less than nor greater
        # than node.value, then we don't need to add it to the bst.

    def delete(self, value):
        """
        Deletes a value from the binary search tree.
        """
        if self._root == None or value == None:
            return
        self._root = self._delete(self._root, value)

    def _delete(self, node, value):
        """
        Recursive helper function for deleting nodes from the binary search
        tree.
        """
        if node == None:
            return None
        if node._value < value:
            node._left = self._delete(node._left, value)
        elif node._value > value:
            node._right = self._delete(node._right, value)
        else:
            if node._left == None:
                return node._right
            if node._right == None:
                return node._left
            temp_node = node
            node = self._min(temp_node._right)
            node._right = self._deleteMin(temp_node._right)
            node._left = temp_node._left
        node._rerank()
        return node

    def deleteMin(self):
        """
        Deletes the minimum node from the binary search tree.
        """
        if self.isEmpty():
            raise NodeNotExistsError('BinarySearchTree underflow error.')
        else:
            self._root = self._deleteMin(self._root)

    def _deleteMin(self, node):
        """
        Deletes the minimum node that is the child of the given node.
        """
        if node._left == None:
            return node._right
        node._left = self._deleteMin(node._left)
        node._rerank()
        return node

    def deleteMax(self):
        """
        Deletes the maximum node from the binary search tree.
        """
        if self.isEmpty():
            raise NodeNotExistsError('BinarySearchTree underflow error.')
        else:
            self._root = self._deleteMax(self._root)

    def _deleteMax(self, node):
        """
        Deletes the maximum node that is the child of the given node.
        """
        if node._right == None:
            return node._left
        node._right = self._deleteMax(node._right)
        node._rerank()
        return node

    def _find_min(self, node, turned=True):
        """
        A helper function for delete() that finds a candidate replacement node.
        """
        if node._left._left == None:
            return node
        else:
            return self._find_min(node._left)

    def find(self, value):
        """
        Finds a value in the binary search tree.  Returns the value if it is
        found in the bst, None otherwise.
        """
        if self._root == None:
            return None
        else:
            result = self._find(self._root, value)
            if result == None:
                return None
            else:
                return result._value

    def _find(self, node, value):
        """
        The recursive helper function for find().
        """
        if node == None:
            return None
        if value > node._value:
            return self._find(node._right, value)
        elif value < node._value:
            return self._find(node._left, value)
        return node

    def isEmpty(self):
        """
        Returns True is the binary search tree is empty, False otherwise.
        """
        return self.size() == 0

    def max(self):
        """
        Gets the maximum node in the binary search tree.
        """
        if self.isEmpty():
            return None
        return self._max(self._root)._value

    def _max(self, node):
        """
        Internal helper function that returns the maximum value that is the
        child of the given node.
        """
        if node._right == None:
            return node
        else:
            return self._max(node._right)

    def min(self):
        """
        Gets the minimum node in the binary search tree.
        """
        if self.isEmpty():
            return None
        return self._min(self._root)._value

    def _min(self, node):
        """
        Internal helper function that returns the minimum value that is the
        child of the given node.
        """
        if node._left == None:
            return node
        else:
            return self._min(node._left)

    def size(self):
        """
        Returns the size of the binary search tree.
        """
        if self._root == None:
            return 0
        else:
            return self._root._rank

    def rank(self, value):
        """
        Returns the number of nodes that are children of this node, inclusive,
        if the node is found in the binary search tree, None otherwise.
        """
        found = self._find(self._root, value)
        if found == None:
            return None
        else:
            return found._rank

class NodeNotExistsError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
