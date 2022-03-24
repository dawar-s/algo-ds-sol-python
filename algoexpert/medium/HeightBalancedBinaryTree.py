# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, is_balanced, height):
        self.is_balanced = is_balanced
        self.height = height


class TreeInfo:
    def __init__(self, is_balanced, height):
        self.is_balanced = is_balanced
        self.height = height


def heightBalancedBinaryTree(tree):
    return heightBalancedBinaryTreeHelper(tree).is_balanced


def heightBalancedBinaryTreeHelper(tree: BinaryTree):
    if tree is None:
        return TreeInfo(True, 0)

    left = heightBalancedBinaryTreeHelper(tree.left)
    right = heightBalancedBinaryTreeHelper(tree.right)

    balanced = left.is_balanced and right.is_balanced and abs(left.height - right.height) <= 1
    height = 1 + max(left.height, right.height)

    return TreeInfo(balanced, height)
