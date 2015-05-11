from .binarysearchtree import BinarySearchTree
import random
import unittest

class BSTTests(unittest.TestCase):
    def setUp(self):
        bst = BinarySearchTree()
        bst.add(1)
        bst.add(2)
        bst.add(3)
        self.bst = bst
        self.randBST = BinarySearchTree()
        self.randElems = list(set([random.randint(0,10000) for x in range(1000)]))
        for e in self.randElems:
            self.randBST.add(e)

    def test_add_one(self):
        bst = BinarySearchTree()
        bst.add(3)
        self.assertEqual(bst._root._value, 3)
        self.assertEqual(bst._root._rank, 1)

    def test_add_three(self):
        bst = BinarySearchTree()
        bst.add(3)
        bst.add(1)
        bst.add(5)
        self.assertEqual(bst._root._value, 3)
        self.assertEqual(bst._root._left._value, 1)
        self.assertEqual(bst._root._right._value, 5)
        self.assertEqual(bst._root._rank, 3)
        self.assertEqual(bst._root._left._rank, 1)
        self.assertEqual(bst._root._right._rank, 1)

    def test_delete(self):
        for elem in self.randElems:
            if random.random() > .5:
                self.randBST.delete(elem)
            else:
                self.assertEqual(elem, self.randBST.find(elem))

    def test_deletemin(self):
        elems = sorted(self.randElems)
        for i in range(len(elems)):
            self.assertEqual(self.randBST.find(elems[i]), elems[i])
            self.randBST.deleteMin()
            self.assertIsNone(self.randBST.find(elems[i]))

    def test_deletemax(self):
        elems = sorted(self.randElems)
        for i in range(0, len(elems), -1):
            self.assertEqual(self.randBST.find(elems[i]), elems[i])
            self.randBST.deleteMax()
            self.assertIsNone(self.randBST.find(elems[i]))

    def test_find_contained_elem(self):
        for e in self.randElems:
            self.assertEqual(e, self.randBST.find(e))

    def test_find_missing_elem(self):
        self.assertIsNone(self.bst.find(11))
        self.assertIsNone(self.bst.find(-1))

    def test_max(self):
        self.assertEqual(max(self.randElems), self.randBST.max())

    def test_min(self):
        self.assertEqual(min(self.randElems), self.randBST.min())

    def test_in_order_traversal(self):
        def to_string(node, acc):
            if acc == "":
                return str(node)
            return acc + "," + str(node)

        self.assertEqual(self.bst.in_order_traversal(to_string, ""), "1,2,3")

    def test_pre_order_traversal(self):
        def to_string(node, acc):
            if acc == "":
                return str(node)
            return acc + "," + str(node)

        self.assertEqual(self.bst.pre_order_traversal(to_string, ""), "1,2,3")

    def test_post_order_traversal(self):
        def to_string(node, acc):
            if acc == "":
                return str(node)
            return acc + "," + str(node)

        self.assertEqual(self.bst.post_order_traversal(to_string, ""), "2,3,1")
