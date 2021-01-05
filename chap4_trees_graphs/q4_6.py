import numpy as np
from binarytree import bst, Node, build

# This question assumes to have access to root node and no access to parent from a node
def find_successor(node, value, queue):
    if node.value > value:
        queue.append(node.left)
        next_node = find_successor(node.left, value, queue)
    elif node.value < value:
        queue.append(node.right)
        next_node = find_successor(node.right, value, queue)
    else:
        next_node = queue.pop()
        if next_node.right is not None:
            node = next_node.right
            while node.left is not None:
                node = node.left
            return node
        while len(queue) > 0:
            if next_node.value <= value:
                next_node = queue.pop()
            else:
                return next_node
    if next_node is not None:
        return next_node if next_node.value > value else None
    else:
        return None


test_tree = bst(height=4, is_perfect=True)
print(test_tree)
value = 7
next_node = find_successor(test_tree, value, [test_tree])
if next_node is not None:
    print("next_node in traversal from ", value, " in BST is ", (next_node.value))
else:
    print("Traversal over")


test_tree = bst(height=3, is_perfect=False)
tree_values = test_tree.values
tree_values = list(filter(None, tree_values))
idx = int(np.random.randint(0, len(tree_values)))
value = tree_values[idx]
print(test_tree, value, tree_values)
next_node = find_successor(test_tree, value, [test_tree])
if next_node is not None:
    print("next_node in traversal from ", value, " in BST is ", (next_node.value))
else:
    print("Traversal over")
