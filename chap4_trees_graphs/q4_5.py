from binarytree import bst, Node, tree


def check_bst(node, min_val, max_val):
    if node is None:
        return True

    if node.left is not None:
        leftside = check_bst(node.left, min_val, node.value)

        if leftside is False:
            return False

    if node.right is not None:
        rightside = check_bst(node.right, node.value, max_val)
        if rightside is False:
            return False

    if (min_val is not None and min_val > node.value) or (
        max_val is not None and max_val < node.value
    ):
        return False

    return True


test_tree = tree(height=4, is_perfect=False)
print(test_tree)
balance = check_bst(test_tree, None, None)
print("Tree is %sBST" % ("" if balance else "not "))


test_tree = bst(height=4, is_perfect=True)
print(test_tree)
balance = check_bst(test_tree, None, None)
print("Tree is %sBST" % ("" if balance else "not "))
