import numpy as np
from binarytree import Node, tree


class BinaryNode(Node):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def check_balance(node):
    leftHeight = check_balance(node.left) if node.left is not None else 0
    rightHeight = check_balance(node.right) if node.right is not None else 0
    if leftHeight is False or rightHeight is False or abs(leftHeight - rightHeight) > 1:
        return False
    else:
        return max(leftHeight, rightHeight) + 1


test_tree = tree(height=4, is_perfect=False)
print(test_tree)
balance = check_balance(test_tree)
print("Tree is %sbalanced" % ("" if balance else "not "))

test_tree = tree(height=4, is_perfect=True)
print(test_tree)
balance = check_balance(test_tree)
print("Tree is %sbalanced" % ("" if balance else "not "))
