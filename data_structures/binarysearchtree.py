import unittest

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
        if self._root == None:
            return
        result = _find(self._root, value)
        if result == None:
            return
        new_val = self._find_min(result._right)
        result._value = new_val._left._value
        new_val._left = None

    def _find_min(self, node):
        """
        A helper function for delete() that finds a candidate replacement node.
        """
        if node._left._left == None:
            return node
        else:
            return _find_min(node._left)

    def find(self, value):
        """
        Finds a value in the binary search tree.  Returns the value if it is
        found in the bst, -1 otherwise.
        """
        if self._root == None:
            return -1
        else:
            result = self._find(self._root, value)
            if result == None:
                return -1
            else:
                return result._value

    def _find(self, node, value):
        """
        The recursive helper function for find().
        """
        if node._value == value:
            return node
        elif value > node._value:
            if node._right == None:
                return None
            else:
                return self._find(node._right, value)
        elif value < node._value:
            if node._left == None:
                return None
            else:
                return self._find(node._left, value)

    def size(self):
        """
        Returns the size of the binary search tree.
        """
        if self._root == None:
            return 0
        else:
            return self._root._rank

class BSTTests(unittest.TestCase):
    def setUp(self):
        self.simpleBST = BinarySearchTree()
        self.simpleElems = [5,3,7,1,9,2,4,6,8,0]
        for e in self.simpleElems:
            self.simpleBST.add(e)

    def test_add_one(self):
        bst = BinarySearchTree()
        bst.add(3)
        self.assertEqual(bst._root._value, 3)

    def test_add_three(self):
        bst = BinarySearchTree()
        bst.add(3)
        bst.add(1)
        bst.add(5)
        self.assertEqual(bst._root._value, 3)
        self.assertEqual(bst._root._left._value, 1)
        self.assertEqual(bst._root._right._value, 5)

    def test_find_contained_elem(self):
        for e in self.simpleElems:
            self.assertEqual(e, self.simpleBST.find(e))

    def test_find_missing_elem(self):
        self.assertEqual(-1, self.simpleBST.find(10))
        self.assertEqual(-1, self.simpleBST.find(-1))