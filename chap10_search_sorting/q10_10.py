from binarytree import Node


class BinaryNode(Node):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.rank = 0


class Stream:
    def __init__(self):
        self.root = None

    def track(self, x):
        if self.root is None:
            self.root = BinaryNode(x)
        else:
            self.insert(self.root, x)

    def insert(self, node, value):
        if value == node.value:
            node.rank += 1
        elif value < node.value:
            node.rank += 1
            if node.left is None:
                node.left = BinaryNode(value)
            else:
                self.insert(node.left, value)
        else:
            if node.right is None:
                node.right = BinaryNode(value)
            else:
                self.insert(node.right, value)

    def getRankItem(self, x):
        if self.root.value == x:
            return self.root.rank
        else:
            return self.findX(self.root, x)

    def findX(self, node, value, rank=0):
        if node.value == value:
            return rank + node.rank
        elif value < node.value:
            return self.findX(node.left, value, rank)
        else:
            return self.findX(node.right, value, rank + node.rank + 1)


array = [5, 1, 4, 4, 5, 9, 7, 13, 3, 10, 6]
stream = Stream()
for elem in array:
    stream.track(elem)
print(stream.root)
num = 6
print("Rank of item %d: %d " % (num, stream.getRankItem(num)))
