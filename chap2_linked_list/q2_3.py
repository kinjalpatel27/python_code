import numpy as np
from linked_list import linked_list


def del_mid_node(node):
    if node.data == None or node.next == None:
        return
    node.data = node.next.data
    node.next = node.next.next


llist = linked_list()
data = np.random.randint(1, 10, 9)
for i in range(len(data)):
    llist.append(data[i])

print("Original linked list", llist)
node = llist.head
for i in range(3):
    node = node.next
del_mid_node(node)
print("After removing 4th node", llist)

node = llist.head
del_mid_node(node)
print("After removing 0th node", llist)

node = llist.head
for i in range(8):
    node = node.next
del_mid_node(node)
print("After removing last node", llist)
