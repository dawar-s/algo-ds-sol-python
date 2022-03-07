# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    sum_array = []
    branchSumsHelper(root, sum_array, 0)
    return sum_array


def branchSumsHelper(tree, sum_array, running_sum):
    if tree is None:
        return
    if tree.left is None and tree.right is None:
        sum_array.append(running_sum + tree.value)
        return
    running_sum += tree.value
    branchSumsHelper(tree.left, sum_array, running_sum)
    branchSumsHelper(tree.right, sum_array, running_sum)

