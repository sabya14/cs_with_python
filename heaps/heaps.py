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
        self.last_element = None  # Maintain the last element in the heap, to quicken removal
        self.last_element_level = None  # level is useful when bubbling down after removal

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
        # Bubble up a newly inserted to its correct position
        if node.parent is not None and (node.value > node.parent.value):
            temp = node.parent.value
            node.parent.value = node.value
            node.value = temp
            self.bubble_up(node.parent)
        else:
            return

    def bubble_down(self, node, level):
        # Bubble up a newly inserted root to its correct position
        if node is None:
            return
        level = level + 1
        if node.left is not None:
            if node.value < node.left.value:
                # Swap value if condition satifies
                temp = node.left.value
                node.left.value = node.value
                node.value = temp
            if level >= self.last_element_level:
                # If this element level is more than the last_element_level, then only change this
                self.last_element = node.left
                self.last_element_level = level

        if node.right is not None:
            if node.value < node.right.value:
                temp = node.right.value
                node.right.value = node.value
                node.value = temp
            if level >= self.last_element_level:
                # If this element level is more than the last_element_level, then only change this
                self.last_element = node.right
                self.last_element_level = level

        # recursively boil down
        self.bubble_down(node.left, level)
        self.bubble_down(node.right, level)

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            self.last_element = self.root
            self.last_element_level = 0
            return
        # Find the next blank position to insert at
        node, pos, level = self.find_insert_point(self.root, 0)
        if pos == 'left':
            node.left = Node(value, parent=node)
            # Always keep reference to last_element node
            self.last_element = node.left
            self.last_element_level = level
            self.bubble_up(node.left)
        else:
            node.right = Node(value, parent=node)
            # Always keep reference to last_element node
            self.last_element = node.right
            self.last_element_level = level
            self.bubble_up(node.right)

    def heapify(self):
        self.bubble_down(self.root)

    def remove_node(self, node):
        # Replace value with last element value
        node.value = self.last_element.value
        last_element_parent = self.last_element.parent
        if last_element_parent.right == self.last_element:
            last_element_parent.right = None
        if last_element_parent.left == self.last_element:
            last_element_parent.left = None
        return node

    def poll(self):
        if self.root is None:
            return ValueError("Heap is empty")
        to_return = self.root
        self.root = self.remove_node(self.root)
        self.bubble_down(self.root, 0)
        return to_return

    def find_node_with_value(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return node
        node_l = self.find_node_with_value(node.left, value)
        if node_l:
            return node_l
        node_r = self.find_node_with_value(node.right, value)
        if node_r:
            return node_r
        return False

    def remove(self, value):
        if self.root is None:
            return ValueError("Heap is empty")
        node = self.find_node_with_value(self.root, value)
        to_return = node
        self.remove_node(node)
        self.bubble_down(self.root, 0)
        return to_return


if __name__ == "__main__":
    b_tree = Heap()
    b_tree.insert(1)
    b_tree.insert(2)
    b_tree.insert(3)
    b_tree.insert(4)
    b_tree.insert(5)
    b_tree.insert(6)
    b_tree.insert(7)
    print(b_tree.remove(3))
    print(b_tree)
    print(b_tree.remove(7))
    print(b_tree)
