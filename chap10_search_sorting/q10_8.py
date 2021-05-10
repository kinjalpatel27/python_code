import numpy as np


def find_dupes(array):
    memory = np.zeros(1000, dtype=np.uint32)
    for elem in array:
        mem_idx = (elem - 1) // 32
        digit = (elem - 1) % 32
        mem_val = memory[mem_idx]
        if mem_val & 1 << digit > 0:
            print("Duplicate", elem)
        else:
            mem_val |= 1 << digit
            memory[mem_idx] = mem_val


total = np.random.randint(1000, 32000)
array = np.random.randint(1, 32000, (total))

find_dupes(array)
