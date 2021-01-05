import numpy as np
from binarytree import Node, tree


class BinaryNode(Node):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class LinkedListNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = LinkedListNode()

    def __repr__(self):
        node = self.head.next
        nodes = []
        while node is not None:
            nodes.append(str(node.data.value))
            node = node.next

        nodes.append("None")
        return " -> ".join(nodes)

    def append(self, data):
        current = self.head
        next_node = LinkedListNode(data)
        while current.next is not None:
            current = current.next

        current.next = next_node


def tree_to_linked_list(root):

    link_lists = []
    link_list = LinkedList()
    link_list.append(root)

    link_lists.append(link_list)

    while True:
        node = link_lists[-1].head
        link_list = LinkedList()
        while node.next is not None:
            left = node.next.data.left
            if left is not None:
                link_list.append(left)
            right = node.next.data.right
            if right is not None:
                link_list.append(right)
            node = node.next
        if link_list.head.next is not None:
            link_lists.append(link_list)
        else:
            break
    return link_lists


test_tree = tree(height=4)
print(test_tree)
linked_lists = tree_to_linked_list(test_tree)
for llist in linked_lists:
    print(llist)
