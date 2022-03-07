def nodeDepths(root):
    sum_array = [0]
    nodeDepthsHelper(root, sum_array, 0)
    return sum_array[0]


def nodeDepthsHelper(tree, sum_array, depth):
    if tree is None:
        return
    sum_array[0] += depth
    nodeDepthsHelper(tree.left, sum_array, depth + 1)
    nodeDepthsHelper(tree.right, sum_array, depth + 1)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
