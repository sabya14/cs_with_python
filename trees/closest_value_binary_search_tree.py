import sys
"""
Write a function that takes in a Binary Search Tree (BST) and a target integer
value and returns the closest value to that target value contained in the BST.
You can assume that there will only be one closest value.</p>

Each BST node has an integer value, a
left child node, and a right child node. A node is
said to be a valid BST node if and only if it satisfies the BST
property: its value is strictly greater than the values of every
node to its left; its value is less than or equal to the values
of every node to its right; and its children nodes are either valid
BST nodes themselves or None / null.
"""

def findClosestValueInBst(tree, target):
    closest_value = sys.maxsize
    traversed_list = [tree.value]
    parse(tree.left, traversed_list)
    parse(tree.right, traversed_list)
    diff_to_target = {x: abs(target - x) for x in traversed_list}
    min_value = min(list(diff_to_target.values()))
    return [k for k, v in diff_to_target.items() if v == min_value][0]


def parse(tree, traversed_list):
    traversed_list.append(tree.value)
    if tree.left != None:
        parse(tree.left, traversed_list)
    if tree.right != None:
        parse(tree.right, traversed_list)


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
