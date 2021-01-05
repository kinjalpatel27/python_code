import numpy as np
from binarytree import Node, tree, bst


def find_ancestor(node, node1, node2):
    if node is None:
        return node
    if node.value == node1 or node.value == node2:
        return node

    x = find_ancestor(node.left, node1, node2)
    y = find_ancestor(node.right, node1, node2)
    if x is not None and y is not None:
        return node
    return y if x is None else x


test_tree = tree(height=4, is_perfect=False)
print(test_tree)
tree_values = test_tree.values
tree_values = list(filter(None, tree_values))
idx1 = int(np.random.randint(0, len(tree_values)))
idx2 = int(np.random.randint(idx1, len(tree_values)))
val1 = tree_values[idx1]
val2 = tree_values[idx2]
ancestor_node = find_ancestor(test_tree, val1, val2)
print("common ancestor between %d and %d  is : %d" % (val1, val2, ancestor_node.value))
