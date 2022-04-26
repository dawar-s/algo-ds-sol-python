class Tree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def maxPathSum(tree: Tree):
    global_max = [float('-inf')]
    helper(tree, global_max)
    return global_max[0]


def helper(tree: Tree, global_max):
    if tree is None:
        return [0, 0, 0]

    left = helper(tree.left, global_max)
    right = helper(tree.right, global_max)

    max_sum_parent_left = max(left[0], left[1]) + tree.value
    max_sum_parent_right = max(right[0], right[1]) + tree.value
    max_sum_parent_left_right = max_sum_parent_left + max_sum_parent_right - tree.value

    lst = [max_sum_parent_left, max_sum_parent_right, max_sum_parent_left_right]

    global_max[0] = max(max(lst), global_max[0])

    return lst
