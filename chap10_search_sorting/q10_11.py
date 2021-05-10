import numpy as np


def create_peak_valley(array):
    idx = 0
    peak = True
    while idx < (len(array) - 1):
        if peak:
            if array[idx] < array[idx + 1]:
                array[idx], array[idx + 1] = array[idx + 1], array[idx]
        else:
            if array[idx] > array[idx + 1]:
                array[idx], array[idx + 1] = array[idx + 1], array[idx]
        peak = not peak
        idx = idx + 1
    return array


test = np.random.randint(0, 10, 11)
print(create_peak_valley(test))
