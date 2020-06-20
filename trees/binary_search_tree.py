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

    def inorder_path(self):
        result = []
        if not self.root:
            return None
        else:
            current = self.root
            self.parse(current, result)
        return result

    def parse(self, current, result):
        if current:
            self.parse(current.left, result)
            print(current.info)
            result.append(current.info)
            self.parse(current.right, result)

    def add(self, element):
        if not self.root:
            self.root = Node(element)
        else:
            current = self.root
            while True:
                if element < current.info:
                    if not current.left:
                        current.left = Node(element)
                        break
                    else:
                        current = current.left
                elif element > current.info:
                    if not current.right:
                        current.right = Node(element)
                        break
                    else:
                        current = current.right
                else:
                    break
