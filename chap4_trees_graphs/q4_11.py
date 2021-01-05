import random
import numpy as np
from binarytree import Node, tree


class BinaryTree:
    def __init__(self, height, is_perfect=False):
        self.root = tree(height, is_perfect=is_perfect)

    # Finds node at random but not with equal probability
    def find_random_node(self, node=None):
        if node is None:
            node = self.root
        options = [None]
        if node.left is not None:
            options.append(node.left)
        if node.right is not None:
            options.append(node.right)

        random.shuffle(options)
        select_node = options[0]
        return node if select_node is None else self.find_random_node(select_node)

    def find(self, node_val):
        def find_node(node_val, node):
            if node.value == node_val:
                return node
            elif node.left is None and node.right is None:
                return None

            if node.left is not None:
                found_node = find_node(node_val, node.left)
                if found_node is not None:
                    return found_node
            if node.right is not None:
                found_node = find_node(node_val, node.right)
                if found_node is not None:
                    return found_node

        return find_node(node_val, self.root)

    def insert(self, new_node):
        node = self.root
        queue = [node]
        while len(queue) > 0:
            node = queue.pop(0)
            if node.left is not None:
                queue.append(node.left)
            else:
                node.left = new_node
                break

            if node.right is not None:
                queue.append(node.right)
            else:
                node.right = new_node
                break

    def delete(self, node_val):
        def delete_node(node, node_val):
            if node.value == node_val:
                if node.left is not None:
                    node.value = node.left.value
                    node_left, found_one = delete_node(node.left, node.left.value)
                    node.left = node_left
                elif node.right is not None:
                    node.value = node.right.value
                    node_right, found_one = delete_node(node.right, node.right.value)
                    node.right = node_right
                else:
                    node = None
                    found_one = 1
                return node, found_one
            if node.left is not None:
                left_node, found_one = delete_node(node.left, node_val)
                if found_one is not None:
                    node.left = left_node
                    return node, 1

            if node.right is not None:
                right_node, found_one = delete_node(node.right, node_val)
                if found_one is not None:
                    node.right = right_node
                    return node, 1
            return None, None

        delete_node(self.root, node_val)


tree = BinaryTree(3)
print(tree.root)
random_node = tree.find_random_node()
found_node = tree.find(random_node.value)

assert random_node.value == found_node.value
tree.insert(Node(55))
tree.insert(Node(105))
tree.insert(Node(125))
print(tree.root)

tree_values = tree.root.values
tree_values = list(filter(None, tree_values))
idx = int(np.random.randint(0, len(tree_values)))
val = tree_values[idx]
print("remove", val)
tree.delete(val)
print(tree.root)
