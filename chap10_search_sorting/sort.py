import numpy as np


def bubble_sort(arry):
    n = len(arry)
    for i in range(n):
        swap = False
        for j in range(n - i - 1):
            if arry[j] > arry[j + 1]:
                arry[j], arry[j + 1] = arry[j + 1], arry[j]
                swap = True
        if not swap:
            break

    return arry


def selection_sort(arry):
    n = len(arry)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arry[min_idx] > arry[j]:
                min_idx = j

        arry[i], arry[min_idx] = arry[min_idx], arry[i]
    return arry


def merge(arry, left, mid, right):
    tmp_arry = []
    idx = mid + 1
    for i in range(left, mid + 1):
        while arry[idx] <= arry[i]:
            tmp_arry.append(arry[idx])
            idx += 1
            if idx > right:
                break

        tmp_arry.append(arry[i])

    for i in range(idx, right + 1):
        tmp_arry.append(arry[i])
    arry[left : right + 1] = np.array(tmp_arry)
    return arry


# does not work for non-unqiue element case
def merge_sort(arry, left=None, right=None):
    if left is None and right is None:
        left = 0
        right = len(arry) - 1

    if left == right:
        return arry

    mid = left + (right - left) // 2
    arry = merge_sort(arry, left, mid)
    arry = merge_sort(arry, mid + 1, right)
    return merge(arry, left, mid, right)


def quick_sort(arry, left_val=None, right_val=None):
    if left_val is None and right_val is None:
        left_val = 0
        right_val = len(arry) - 1

    if right_val - left_val < 1:
        return arry

    left = left_val
    right = right_val
    pivot = arry[right]
    while right - left > 0:
        while arry[left] <= pivot:
            if left >= right:
                break
            left += 1

        while arry[right] > pivot:
            if right <= left:
                break
            right -= 1
        if arry[left] > pivot and arry[right] <= pivot:
            arry[left], arry[right] = arry[right], arry[left]

    arry = quick_sort(arry, left_val, left - 1)
    arry = quick_sort(arry, right, right_val)
    return arry


def radix_sort(arry):
    arry = np.array(arry)
    update = True
    pos = 1

    radix_arry = arry // pos
    while update:
        tmp_arry = np.zeros(len(arry))
        num = 0
        idx = 0
        while num < 10:
            for i in range(len(radix_arry)):
                if radix_arry[i] % 10 == num:
                    tmp_arry[idx] = arry[i]
                    idx += 1
            num += 1

        arry = tmp_arry
        pos *= 10
        radix_arry = arry // pos
        update = False
        for elem in radix_arry:
            if elem != 0:
                update = True

    return arry


arry = [38, 42, 2, 5, 60, 89, 400, 255]
print(radix_sort(arry))
# print(merge_sort(arry))
