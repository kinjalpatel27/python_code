import numpy as np

paren_pairs = []


def parens(n, tmp_paren="", left=None, right=None):
    global paren_pairs

    if left is None and right is None:
        left = n
        right = n
    if left == 0 and right == 0:
        paren_pairs.append(tmp_paren)
    elif left * right < 0 or right < left:
        return
    else:
        parens(n, tmp_paren + "(", left - 1, right)
        parens(n, tmp_paren + ")", left, right - 1)

    return paren_pairs


print(parens(3))
