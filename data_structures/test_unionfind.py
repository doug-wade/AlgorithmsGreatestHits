import unittest
from .unionfind import UnionFind

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

    def test_add(self):
        uf = UnionFind([])
        for n in self.nodes:
            uf.add(n)
        uf.union('a', 'b')
        uf.union('c', 'd')
        uf.union('a', 'd')
        uf.union('e', 'f')
        uf.union('g', 'h')
        uf.union('f', 'h')
        uf.union('c', 'g')
        #should be fully connected
        leader = None
        for node in self.nodes:
            if leader:
                self.assertEqual(leader, uf.find(node))
            else:
                leader = uf.find(node)
