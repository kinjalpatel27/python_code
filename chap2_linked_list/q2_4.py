import numpy as np
from linked_list import linked_list


def partition(llist, element):
    left = None
    right = None
    right_head = None
    left_head = None
    current = llist.head
    while current.next is not None:
        if current.next.data < element:
            if left is not None:
                left.next = current.next
            left = current.next
            if left_head is None:
                left_head = left
        else:
            if right is not None:
                right.next = current.next
            right = current.next
            if right_head is None:
                right_head = right
        current = current.next

    left.next = right_head
    llist.head.next = left_head
    right.next = None


llist = linked_list()
data = [3, 5, 8, 5, 10, 2, 1]
for i in range(len(data)):
    llist.append(data[i])
print("Original linked list", llist)
partition(llist, 5)
print("Partitioned linked list", llist)

llist = linked_list()
data = np.random.randint(1, 10, 9)
for i in range(len(data)):
    llist.append(data[i])
print("Original linked list", llist)
partition(llist, 3)
print("Partitioned linked list", llist)
