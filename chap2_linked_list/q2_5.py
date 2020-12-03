import numpy as np
from linked_list import linked_list


def reverse_sum(llist1, llist2):
    ans = linked_list()
    temp_buf = 0
    curr1 = llist1.head
    curr2 = llist2.head
    while curr1.next is not None or curr2.next is not None:
        if curr1.next is not None:
            data1 = curr1.next.data
            curr1 = curr1.next
        else:
            data1 = 0

        if curr2.next is not None:
            data2 = curr2.next.data
            curr2 = curr2.next
        else:
            data2 = 0

        data = data1 + data2

        ans.append(data % 10 + temp_buf)
        temp_buf = data // 10

    if temp_buf > 0:
        ans.append(temp_buf)
    return ans


llist1 = linked_list()
llist1.append(9)
llist1.append(7)
llist1.append(8)

llist2 = linked_list()
llist2.append(6)
llist2.append(8)
llist2.append(5)

ans = reverse_sum(llist1, llist2)
print(llist1, " + ", llist2, " = ", ans)


def reverse(llist):
    current = llist.head.next
    process = current.next

    while process.next is not None:
        next1 = process.next
        process.next = current
        if llist.head.next == current:
            current.next = None

        current = process
        process = next1

    process.next = current
    llist.head.next = process


reverse(llist1)
reverse(llist2)
ans = reverse_sum(llist1, llist2)
reverse(ans)
print(llist1, " + ", llist2, " = ", ans)
