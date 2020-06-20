from unittest import TestCase

from trees.binary_search_tree import BinarySearchTree


class TestBinarySearchTree(TestCase):
    def test_inorder_path(self):
        tree = BinarySearchTree()
        elements = [4, 2, 3, 1, 7, 6]
        for element in elements:
            tree.add(element)
        path = tree.inorder_path()
        self.assertListEqual(path, [1, 2, 3, 4, 6, 7])