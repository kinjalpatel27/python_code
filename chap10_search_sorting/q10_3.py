import random
import numpy as np


def rotate(a, n=1):
    if len(a) == 0:
        return a
    n = -n % len(a)  # flip rotation direction
    return a[n:] + a[:n]


cnt = 0


def find_element(array, elem, left_idx=None, right_idx=None):
    global cnt
    if left_idx == None:
        left_idx = 0
        right_idx = len(array) - 1
        if array[left_idx] == elem:
            return left_idx
        if array[right_idx] == elem:
            return right_idx

    idx = (left_idx + right_idx) // 2

    if array[idx] == elem:
        return idx

    if abs(right_idx - left_idx) < 1 or right_idx < left_idx:
        return None
    cnt += 1
    # print("left %d : %d"%(left_idx,array[left_idx]),"right %d : %d"%(right_idx,array[right_idx]),"%d : %d"%(idx,array[idx]),elem)
    if array[left_idx] > array[right_idx] and array[right_idx] > elem:
        tmp_idx = find_element(array, elem, idx + 1, right_idx)
        if tmp_idx is None:
            tmp_idx = find_element(array, elem, left_idx, idx - 1)
        idx = tmp_idx
    else:
        tmp_idx = find_element(array, elem, left_idx, idx - 1)
        if tmp_idx is None:
            tmp_idx = find_element(array, elem, idx + 1, right_idx)
        idx = tmp_idx

    return idx


N = 32
array = np.random.randint(1, 50, N).tolist()
array = sorted(array)
rotation = random.sample(range(0, N), 1)[0]

array = rotate(array, rotation)

# array = [45, 45, 47, 4, 8, 11, 12, 13, 13, 14, 16, 19, 20, 20, 23, 23, 24, 25, 26, 26, 27, 31, 32, 32, 33, 33, 35, 39, 42, 42, 43, 44]
elem = array[random.sample(range(0, N), 1)[0]]
print(array, elem)
idx = find_element(array, elem)

assert array[idx] == elem
print("Total Trials", cnt, "\nIndex No.", idx)
