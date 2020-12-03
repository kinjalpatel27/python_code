import numpy as np
from linked_list import linked_list


def llist_len(llist):
    length = 0
    curr = llist.head
    while curr.next is not None:
        length += 1
        curr = curr.next
    return length


def get_kthnode(tmp, k):
    for _ in range(k):
        tmp = tmp.next
    return tmp


def intersect(llist1, llist2):
    len1 = llist_len(llist1)
    len2 = llist_len(llist2)

    tmp1 = llist1.head if len1 <= len2 else get_kthnode(llist1.head, (len1 - len2))
    tmp2 = llist2.head if len2 <= len1 else get_kthnode(llist2.head, (len2 - len1))

    while tmp1.next is not None:
        if tmp1.next == tmp2.next:
            return tmp1.next
        else:
            tmp1 = tmp1.next
            tmp2 = tmp2.next
    return -1


def print_node(llist1, llist2, node):
    if hasattr(node, "data"):
        print("\nIntersection between: ")
        print(llist1)
        print(llist2)
        print("Intersecting node :", node.data)
    else:
        print("\nNo intersection between")
        print(llist1)
        print(llist2)


data1 = [2, 4, 5, 6]
data2 = [9, 3, 1, 0, 10, 7]

llist1 = linked_list()
llist2 = linked_list()
for d in data1:
    llist1.append(d)

for d in data2:
    llist2.append(d)

# create an intersection between two lists
tmp1 = llist1.head
for _ in range(2):
    tmp1 = tmp1.next

tmp2 = llist2.head
for _ in range(3):
    tmp2 = tmp2.next

node = intersect(llist1, llist2)
print_node(llist1, llist2, node)

tmp2.next = tmp1
node = intersect(llist1, llist2)
print_node(llist1, llist2, node)
