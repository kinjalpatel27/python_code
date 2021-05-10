import collections
import numpy as np


def if_anagram(st1, st2):
    if len(st1) != len(st2):
        return False
    if sorted(st1) != sorted(st2):
        return False
    return True


def sort_arry(arry):

    idx1 = 0
    arry = sorted(arry)
    anag_dict = collections.defaultdict(list)
    while idx1 < len(arry):
        idx2 = idx1 + 1
        anag_dict[arry[idx1]].append(arry[idx1])
        while idx2 < len(arry):
            if if_anagram(arry[idx1], arry[idx2]):
                if arry[idx1] > arry[idx2]:
                    anag_dict[arry[idx2]] = anag_dict.pop(arry[idx1])
                    anag_dict[arry[idx2]].append(arry[idx2])
                else:
                    anag_dict[arry[idx1]].append(arry[idx2])
                arry.pop(idx2)
            else:
                idx2 += 1
        idx1 += 1

    sorted_arry = []
    for key in anag_dict.keys():
        sorted_arry.append(key)
        for elem in anag_dict[key]:
            if elem != key:
                sorted_arry.append(elem)
    return sorted_arry


arry = ["kalt", "car", "bus", "cub", "sub", "test", "talk", "arc"]
print(sort_arry(arry))
