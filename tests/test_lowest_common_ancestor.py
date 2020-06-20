from unittest import TestCase

from trees.lowest_common_ancestor import BinarySearchTree, lca, lca_iterative


class Test(TestCase):
    def test_lca(self):
        tree = BinarySearchTree()
        input_data = [4, 2, 3, 1, 7, 6]
        for i in input_data:
            tree.create(i)
        lca_node = lca(tree.root, 1, 7)
        self.assertEqual(lca_node.info, 4)

    def test_lca_only_right_side_present(self):
        tree = BinarySearchTree()
        input_data = [1, 2, 3, 4, 5, 6]
        for i in input_data:
            tree.create(i)
        lca_node = lca(tree.root, 5, 6)
        self.assertEqual(5, lca_node.info)

    def test_lca_iterative(self):
        tree = BinarySearchTree()
        input_data = [4, 2, 3, 1, 7, 6]
        for i in input_data:
            tree.create(i)
        lca_node = lca_iterative(tree.root, 1, 7)
        self.assertEqual(lca_node.info, 4)

    def test_lca_only_right_side_present(self):
        tree = BinarySearchTree()
        input_data = [1, 2, 3, 4, 5, 6]
        for i in input_data:
            tree.create(i)
        lca_node = lca_iterative(tree.root, 5, 6)
        self.assertEqual(5, lca_node.info)