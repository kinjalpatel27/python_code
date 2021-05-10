import numpy as np


row = 8
col = 10

path = []
fail_points = {}


def gen_grid():
    mat = np.ones((row, col), np.int8)

    off_limit_cells = 15
    for _ in range(off_limit_cells):
        i = np.random.randint(1, row)
        j = np.random.randint(1, col)
        mat[i, j] = 0
    return mat


def find_path(mat, i, j):

    if i < 0 or j < 0:
        return False
    if mat[i, j] == 0:
        return False
    if (i, j) in fail_points:
        return False
    dest = True if i == 0 and j == 0 else False

    if dest or find_path(mat, i - 1, j) or find_path(mat, i, j - 1):
        path.append([i, j])
        return True
    fail_points[(i, j)] = 1
    return False


mat = gen_grid()
print("Grid \n", mat)
valid = find_path(mat, row - 1, col - 1)
print("Path is:", path)
