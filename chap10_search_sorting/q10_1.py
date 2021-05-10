import numpy as np
from sort import merge_sort


def sort_arry(arry1, arry2):
    idx2 = len(arry2) - 1
    idx1 = len(arry1) - len(arry2) - 1
    assert idx1 > 0
    idx = len(arry1) - 1
    while idx >= 0:
        if arry2[idx2] > arry1[idx1]:
            arry1[idx] = arry2[idx2]
            idx -= 1
            idx2 = idx2 - 1
            if idx2 < 0:
                while idx >= 0:
                    arry1[idx] = arry1[idx1]
                    idx -= 1
                    idx1 = idx1 - 1
        else:
            arry1[idx] = arry1[idx1]
            idx -= 1
            idx1 = idx1 - 1
            if idx1 < 0:
                while idx >= 0:
                    arry1[idx] = arry2[idx2]
                    idx -= 1
                    idx2 = idx2 - 1
    return arry1


arryA = np.sort(np.random.randint(0, 50, 10)).tolist()
arryB = np.sort(np.random.randint(0, 50, 6)).tolist()


for _ in range(len(arryB)):
    arryA.append(None)
print(arryA, arryB)
print(sort_arry(arryA, arryB))
