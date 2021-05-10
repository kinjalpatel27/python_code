from copy import deepcopy

queen_pos = []


def arrange_queens(n, col=0, sel_row={}, diff={}, comb=[]):
    global queen_pos
    if col == n:
        queen_pos.append(deepcopy(comb))
        return

    for row in range(n):
        if not (row in sel_row or (row - col) in diff):
            sel_row[row] = 1
            diff[row - col] = 1
            comb.append((row, col))
            arrange_queens(n, col + 1, sel_row, diff, comb)
            del sel_row[row]
            del diff[row - col]
            comb.pop(-1)

    return


arrange_queens(8)
print(queen_pos)
