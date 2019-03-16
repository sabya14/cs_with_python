"""
A pythonic representation of linked list
"""


class Node:

    def __init__(self, value, _next=None):
        self.value = value
        self._next = _next

    def __repr__(self):
        return self.value

    def __str__(self):
        return self.value


class LinkedList:

    def __init__(self):
        self.head = None

    def __repr__(self):
        _str = ""
        node_to_print = self.head
        while node_to_print:
            _str = f"{_str}{node_to_print.value}=>"
            node_to_print = node_to_print._next
        _str = _str + "None"
        return _str

    def insert(self, value):
        if not self.head:
            self.head = Node(value)
            return
        node_to_insert = self.head
        while node_to_insert._next is not None:
            node_to_insert = node_to_insert._next
        node_to_insert._next = Node(value=value, _next=None)

    def remove(self, value):
        curr_node = self.head
        prev_node = None
        while curr_node and curr_node.value != value:
            prev_node = curr_node
            curr_node = curr_node._next
        if curr_node.value != value:
            raise ValueError("Element to delete not found")
        else:
            if prev_node:
                prev_node._next = curr_node._next
            else:
                self.head = curr_node._next


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert(5)
    linked_list.insert(10)
    linked_list.insert(15)
    linked_list.insert(20)
    print(linked_list)
    linked_list.remove(15)
    print(linked_list)
    linked_list.remove(20)
    linked_list.remove(5)
    print(linked_list)
