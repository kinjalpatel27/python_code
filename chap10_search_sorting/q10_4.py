import random
import numpy as np


def elementAt(array, idx):
    if idx is None:
        return None
    if idx >= len(array):
        return -1
    else:
        return array[idx]


def sortedSearch(array, elem):
    idx = 1
    while elementAt(array, idx) != -1 and elementAt(array, idx) < elem:
        idx *= 2
    low = 0
    high = idx
    trial = 0
    while low <= high:
        trial += 1
        idx = (low + high) // 2
        elem_at_idx = elementAt(array, idx)
        if elem_at_idx == elem:
            break
        if elem_at_idx == -1 or elem_at_idx > elem:
            high = idx - 1
        else:
            low = idx + 1

    print("Total trial : ", trial)
    return idx


N = 42
array = sorted(np.random.randint(1, 50, N).tolist())
elem = array[random.sample(range(0, N), 1)[0]]
print(array, elem)
idx = sortedSearch(array, elem)
assert array[idx] == elem
