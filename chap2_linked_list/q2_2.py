import numpy as np
from linked_list import linked_list


def print_kth_last(llist, k):
    current = llist.head
    kth_elem = current
    count = 0
    length = 0
    while current.next is not None:
        count += 1
        if count == k:
            count -= 1
            kth_elem = kth_elem.next
        length += 1
        current = current.next
    if k > length:
        print("Invalid K value")
    else:
        print("Kth Element ", kth_elem.data)


llist = linked_list()
data = np.random.randint(1, 10, 9)
for i in range(len(data)):
    llist.append(data[i])

print("Original linked list", llist)
print_kth_last(llist, 1)
