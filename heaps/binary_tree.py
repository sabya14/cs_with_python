"""
A basic implementation of a binary tree in Python using linked lists.
Points - Each node should have max two children.
       - The tree should be complete from the left most side.
"""


class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        if self.value is None:
            return "None"
        else:
            return str(self.value)


class BinaryTree:

    def __init__(self):
        self.root = None

    def find_insert_point(self, node, level):
        if not node.left:
            return node, 'left', level + 1
        if not node.right:
            return node, 'right', level + 1
        else:
            node_l, pos_l, _level_l = self.find_insert_point(node.left, level + 1)
            node_r, pos_r, _level_r = self.find_insert_point(node.right, level + 1)
            if _level_l <= _level_r:
                return node_l, pos_l, _level_l
            else:
                return node_r, pos_r, _level_r

    def in_order(self, node):
        _str = ""
        if node.left:
            _str = _str + self.in_order(node.left)
        _str = _str + str(node) + " "
        if node.right:
            _str = _str + self.in_order(node.right)
        return _str

    def __str__(self):
        if not self.root:
            return "Empty tree"
        return self.in_order(self.root)

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            print(self.root)
            return
        node, pos, level = self.find_insert_point(self.root, 0)
        if pos == 'left':
            node.left = Node(value)
        else:
            node.right = Node(value)


if __name__ == "__main__":
    b_tree = BinaryTree()
    b_tree.insert(0)
    b_tree.insert(1)
    b_tree.insert(2)
    b_tree.insert(3)
    b_tree.insert(4)
    b_tree.insert(5)
    print(b_tree)
