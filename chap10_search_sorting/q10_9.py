import numpy as np

cnt = 0


def matSearch(mat, elem, left=None, right=None):
    global cnt
    cnt += 1
    if left is None:
        left = (0, 0)
        right = (mat.shape[0] - 1, mat.shape[1] - 1)

    mid = ((left[0] + right[0]) // 2, (left[1] + right[1]) // 2)

    if right[0] - left[0] < 2 or right[1] - left[1] < 2:
        found = False
        for row_idx in range(left[0], right[0] + 1):
            for col_idx in range(left[1], right[1] + 1):
                if mat[row_idx, col_idx] == elem:
                    found = True
                    loc = (row_idx, col_idx)
                    break
        if found:
            return loc
        else:
            return None

    if mat[mid] < elem:
        # 2nd
        loc = matSearch(mat, elem, (left[0], mid[1] + 1), (mid[0], right[1]))
        if loc is None:
            # 3rd
            loc = matSearch(mat, elem, (mid[0] + 1, left[1]), (right[0], mid[1]))
        if loc is None:
            # 4th
            loc = matSearch(mat, elem, (mid[0] + 1, mid[1] + 1), right)

    elif mat[mid] > elem:
        # 1st
        loc = matSearch(mat, elem, left, mid)
        if loc is None:
            # 2nd
            loc = matSearch(mat, elem, (left[0], mid[1]), (mid[0], right[1]))
        if loc is None:
            # 3rd
            loc = matSearch(mat, elem, (mid[0], left[1]), (right[0], mid[1]))
    else:
        return mid

    return loc


H = 16
W = 16
mat = np.random.randint(0, 100, (H, W))

mat = np.sort(mat, axis=0)
mat = np.sort(mat, axis=1)

print(mat)
row_idx = np.random.randint(0, H)
col_idx = np.random.randint(0, W)
print(row_idx, col_idx, mat[row_idx, col_idx])
idx = matSearch(mat, mat[row_idx, col_idx])
print(idx, mat[idx])
