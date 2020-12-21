import numpy as np
from binarytree import Node


class BinaryNode(Node):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


array = np.arange(7)


def tree(left, right, array):
    if right < left:
        return None
    idx = (left + right) // 2
    node = BinaryNode(array[idx])

    node.left = tree(left, idx - 1, array)
    node.right = tree(idx + 1, right, array)
    return node


root = tree(0, len(array) - 1, array)

print(root)
