from collections import defaultdict
from binarytree import Node, tree

no_path = 0


def remove_element(running_sum1, require_sum, path_list, value):
    global no_path
    if running_sum1 - require_sum in list(path_list.keys()):
        no_path += 1

    if len(path_list[running_sum1]) > 1:
        path_list[running_sum1].remove(value)
    else:
        path_list.pop(running_sum1, value)

    return path_list


def find_sum_path(node, require_sum, running_sum=0, path_list=None):
    global no_path
    if path_list is None:
        path_list = defaultdict(list)
        if node.value == require_sum:
            no_path += 1

    if node is None:
        return None, running_sum
    else:
        path_list[running_sum + node.value].append(node.value)
        running_sum += node.value

    value, running_sum1 = find_sum_path(node.left, require_sum, running_sum, path_list)
    if value is not None:
        path_list = remove_element(running_sum1, require_sum, path_list, value)

    value, running_sum1 = find_sum_path(node.right, require_sum, running_sum, path_list)
    if value is not None:
        path_list = remove_element(running_sum1, require_sum, path_list, value)
    return node.value, running_sum


test_tree = tree(4)
require_sum = 16
print(test_tree)

find_sum_path(test_tree, require_sum, running_sum=0, path_list=None)
print("Number of path with sum %d is %d" % (require_sum, no_path))
