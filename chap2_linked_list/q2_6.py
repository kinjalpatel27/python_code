from linked_list import linked_list


def reverse_from_start(llist):
    current = llist.head.next
    # If the length of list is 1, return 1st element
    if current.next is None:
        return current

    process = current.next
    if process.next is None:
        return process
    fast = process.next
    # If there are only 3 elements, return middle element
    if fast.next is None:
        return process

    total = 3
    while fast.next is not None:
        tmp = process.next
        process.next = current
        if fast.next.next is None:
            total += 1
            break
        fast = fast.next.next
        total += 2

        current = process
        process = tmp

    mid = llist.head.next if total % 2 == 0 else tmp
    llist.head.next.next = tmp
    llist.head.next = process if total % 2 == 0 else current
    return mid


def check_palindrom(llist, mid):
    head = llist.head
    tail = mid
    if tail.next is None:
        return True if head.next.data == tail.data else False

    while tail.next is not None:
        if head.next.data != tail.next.data:
            return False
        head = head.next
        tail = tail.next

    if head == mid or head.next == mid:
        return True
    else:
        return False


datas = ["abclllpcba", "abcllcba", "abclalcba", "abka", "aba", "aa", "a"]

for data in datas:
    llist = linked_list()
    for i in range(len(data)):
        llist.append(data[i])

    mid = reverse_from_start(llist)
    palin = check_palindrom(llist, mid)
    ans = "" if palin else "not"

    print("%s is %s palindrom" % (data, ans))
