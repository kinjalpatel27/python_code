class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self):
        self.head = node()

    def __repr__(self):
        node = self.head.next
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next

        nodes.append("None")
        return " -> ".join(nodes)

    def append(self, data):
        current = self.head

        next_node = node(data)
        while current.next is not None:
            current = current.next
        current.next = next_node
