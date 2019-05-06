"""
Problem Statement - 2.5 from the book of cracking the coding interview
e.g two linked list 1 -> 2 -> 3 and 1 -> 9 -> 2 should give result 291 + 321 ->  2 -> 1 -> 6
"""


class Node:
    def __init__(self, value, next_node=None):
        self.data = value
        self.next = next_node

    def __str__(self):
        return str(self.data)


def sum_list(list_a, list_b):
    result = LinkedList()
    count = 0
    # Add check for one list as null
    node_a = list_a.head
    node_b = list_b.head

    # Calculate the head
    sum = 0
    if not result.head:
        sum += (10 ** count) * (node_a.data + node_b.data)
        result.head = Node(int(sum / (10 ** count)) % 10)
        count += 1
    pointer = result.head
    node_a = node_a.next
    node_b = node_b.next
    # Then calculate the next once
    while node_a or node_b:
        if node_a:
            data_a = node_a.data
            node_a = node_a.next
        else:
            data_a = 0
        if node_b:
            data_b = node_b.data
            node_b = node_b.next
        else:
            data_b = 0
        sum += (10 ** count) * (data_a + data_b)
        pointer.next = Node(int(sum / (10 ** count)) % 10)
        count += 1
        pointer = pointer.next
    print(sum)
    result.print()


class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, value):
        if not self.head:
            self.head = Node(value=value)
            return
        pointer = self.head
        while pointer.next:
            pointer = pointer.next
        pointer.next = Node(value)

    def print(self):
        pointer = self.head
        if not pointer:
            print("Emoty linked list")
            return
        while pointer:
            print(f"{pointer} -> ", end=" ")
            pointer = pointer.next
        print("null")


list_a = LinkedList()
list_a.insert(1)
list_a.insert(2)
list_a.insert(3)
list_b = LinkedList()
list_b.insert(1)
list_b.insert(9)
list_b.insert(2)
list_b.insert(1)
list_a.print()
list_b.print()
sum_list(list_a, list_b)
