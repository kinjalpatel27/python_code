import numpy as np


def triple_step(n, keep=None):
    if keep is None:
        keep = np.ones(n + 1, np.int8) * (-1)

    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif keep[n] > -1:
        return keep[n]
    else:
        keep[n] = (
            triple_step(n - 1, keep)
            + triple_step(n - 2, keep)
            + triple_step(n - 3, keep)
        )
        return keep[n]


print("Number of combinations", triple_step(6))
