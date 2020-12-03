import numpy as np
from linked_list import linked_list

DEBUG = False


def remove_dup_hashmap(llist):
    # O(N) time
    hashmap = {}
    current = llist.head
    while current.next is not None:
        # if the key already exist in hashmap, we found a duplicate and remove
        # it by setting the next element to next-to-next,
        # else add the key in hash table and move to the next one for checking
        if current.next.data in list(hashmap.keys()):
            current.next = current.next.next
        else:
            hashmap[current.next.data] = current.next.next
            current = current.next

    return llist


def remove_dup_notmp(llist):
    # O(N^2) time, O(1) space
    current = llist.head
    runner = current.next
    # the current.next data will be compared to each key in the chain for
    # finding duplicates
    while current.next is not None:
        while runner.next is not None:
            if current.next.data == runner.next.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
        runner = current.next

    return llist


llist = linked_list()
data = np.random.randint(1, 10, 9)

datas = [
    [1, 2, 3, 4, 5, 6, 7, 8],
    [0],
    [1, 1, 1, 1, 1],
    [1, 2, 3, 4, 5, 3],
    [2, 1, 2, 2, 3, 2, 4, 1],
    [],
    data,
]
for data in datas:
    llist = linked_list()
    for d in data:
        llist.append(d)

    remove_dup_llist1 = remove_dup_hashmap(llist)
    remove_dup_llist2 = remove_dup_notmp(llist)
    assert remove_dup_llist1 == remove_dup_llist2
    if DEBUG:
        print("Original linked list", llist)
        print("After removing duplicates (O(N)) : ", remove_dup_llist1)
        print(
            "After removing duplicates (O(N^2)) (No temp buffer): ", remove_dup_llist2
        )
