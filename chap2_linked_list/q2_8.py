from linked_list import linked_list


def find_circular(llist):
    slow = llist.head.next
    if slow.next.next is not None:
        fast = slow.next.next
    else:
        return -1

    while fast.next is not None:
        if slow == fast or slow.next == fast:
            return slow
        if fast.next.next is None:
            return -1
        slow = slow.next

        fast = fast.next.next

    return -1


llist = linked_list()
data = "abcdef"
for d in data:
    llist.append(d)

# Find an intermediate node to circle around
tmp = llist.head
for _ in range(3):
    tmp = tmp.next

# find the last node and assign intermediate node as next to create a circular
# linked list
last = llist.head
while last.next is not None:
    last = last.next

last.next = tmp

circle_node = find_circular(llist)

assert circle_node.data == tmp.data
if hasattr(circle_node, "data"):
    print("\nIntersection between Node", circle_node.data)
else:
    print("\nNot a circular linked list")
