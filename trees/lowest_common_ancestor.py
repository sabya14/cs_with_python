class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def lca(root, v1, v2):
    current = root
    if v1 < current.info and v2 < current.info:
        return lca(current.left, v1, v2)
    elif v1 > current.info and v2 > current.info:
        return lca(current.right, v1, v2)
    else:
        return current


def lca_iterative(root, v1, v2):
    current = root
    while True:

        if v1 < current.info and v2 < current.info:
            current = current.left
        elif v1 > current.info and v2 > current.info:
            current = current.right
        else:
            return current
            break


