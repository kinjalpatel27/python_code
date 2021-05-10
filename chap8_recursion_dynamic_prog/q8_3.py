import numpy as np
import random


def magic_idx(magic_arry, low_idx=None, high_idx=None):

    if low_idx is None and high_idx is None:
        low_idx = 0
        high_idx = len(magic_arry) - 1

    if low_idx > high_idx:
        return -1

    idx = (high_idx + low_idx) // 2

    idx_val = magic_arry[idx]

    if idx_val == idx:
        return idx
    leftidx = min(idx - 1, idx_val)
    ind = magic_idx(magic_arry, low_idx, leftidx)
    if ind >= 0:
        return ind

    rightidx = max(idx + 1, idx_val)
    ind = magic_idx(magic_arry, rightidx, high_idx)

    return ind


n_elem = 100
magic_num = np.random.randint(1, n_elem - 2)
magic_arry = []
if magic_num > 0:
    magic_arry = sorted(random.sample(range(-n_elem, magic_num - 2), (magic_num)))
magic_arry.append(magic_num)

if magic_num < n_elem:
    arry = sorted(
        random.sample(range(magic_num + 2, n_elem + 100), (n_elem - magic_num))
    )
magic_arry.extend(arry)
magic_arry[magic_num + 1] = magic_num
magic_arry[magic_num + 2] = magic_num
magic_arry[magic_num + 3] = magic_num
idx = magic_idx(magic_arry)

if idx == -1:
    AssertionError("Could not Find Magic Index")
assert magic_num == idx
