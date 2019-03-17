"""
A basic implementation of a heap data structure in Python using pointer based nodes.
We will be implementing an min heap.
Points - Each node should have max two children, and there value should be less than or equal to the parent node.
       - The heap should be complete from the left most side.
"""


class Node:

    def __init__(self, value, parent=None, left=None, right=None):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

    def __str__(self):
        if self.value is None:
            return "None"
        else:
            if self.parent is not None:
                return f"{str(self.value)}({self.parent.value}) "
            else:
                return f"{str(self.value)}(Root) "


class Heap:

    def __init__(self):
        self.root = None
        self.last_insert = None

    def find_insert_point(self, node, level):
        # Recursively find the next best position to insert
        # If left blank insert there
        if not node.left:
            return node, 'left', level + 1
        # If right blank insert there
        if not node.right:
            return node, 'right', level + 1
        else:
            # From the left or right branch, find the best leftest node with the least level
            node_l, pos_l, _level_l = self.find_insert_point(node.left, level + 1)
            node_r, pos_r, _level_r = self.find_insert_point(node.right, level + 1)
            if _level_l <= _level_r:
                return node_l, pos_l, _level_l
            else:
                return node_r, pos_r, _level_r

    def in_order(self, node):
        # Display the internal tree of the heap in a in order fashion
        _str = ""
        if node.left:
            _str = _str + self.in_order(node.left)
        _str = _str + str(node)
        if node.right:
            _str = _str + self.in_order(node.right)
        return _str

    def __str__(self):
        # Textual representation of the heap in  in_order.
        if not self.root:
            return "Empty tree"
        return self.in_order(self.root)

    def bubble_up(self, node):
        if node.parent is not None and (node.value > node.parent.value):
            temp = node.parent.value
            node.parent.value = node.value
            node.value = temp
            self.bubble_up(node.parent)
        else:
            return

    def bubble_down(self, node):
        if node is None:
            return
        if node.left is not None and (node.value < node.left.value):
            temp = node.left.value
            node.left.value = node.value
            node.value = temp
        if node.right is not None and (node.value < node.right.value):
            temp = node.right.value
            node.right.value = node.value
            node.value = temp

        self.bubble_down(node.right)
        self.bubble_down(node.left)

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            self.last_insert = self.root
            return
        # Find the next blank position to insert at
        node, pos, level = self.find_insert_point(self.root, 0)
        if pos == 'left':
            node.left = Node(value, parent=node)
            # Always keep reference to last inserted node
            self.last_insert = node.left
            self.bubble_up(node.left)
        else:
            node.right = Node(value, parent=node)
            # Always keep reference to last inserted node
            self.last_insert = node.right
            self.bubble_up(node.right)

    def poll(self):
        if self.last_insert.parent:
            # Here we remove the last inserted element from its parent node.
            # Find the parent node of the last element. Then make its appropriate child none.
            # First try and check if the last inserted element was in the right node,
            # We try from right because the heap is always a complete node.
            # If not in right node it must be in the left node.
            parent = self.last_insert.parent
            if parent.right:
                parent.right = None
            else:
                parent.right = None
                parent.left = None

        # Now we make the last inserted element its root node.
        to_return = self.root
        # New root defined
        self.root = self.last_insert
        self.root.parent = None
        # Give left and right of older root to new root
        self.root.left = to_return.left
        self.root.right = to_return.right

        # Give the new root to the children of the older root
        self.root.left.parent = self.root
        self.root.right.parent = self.root
        print("Before bubble down", self)
        self.bubble_down(self.root)
        return to_return

 
if __name__ == "__main__":
    b_tree = Heap()
    b_tree.insert(0)
    b_tree.insert(1)
    b_tree.insert(4)
    b_tree.insert(5)
    b_tree.insert(2)
    b_tree.insert(3)
    print(b_tree.last_insert)
    print("Actual", b_tree)
    print(b_tree.poll())
    print("After polling", b_tree)
    b_tree.insert(5)
    print("Should be like actual again", b_tree)
