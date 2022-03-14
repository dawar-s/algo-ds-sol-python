# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    max_diameter = [0]
    binaryTreeDiameterHelper(tree, max_diameter)
    return max_diameter[0]


def binaryTreeDiameterHelper(tree, max_diameter):
    # Base case, return -1
    # basically this means that 'None' node height is -1
    if tree is None:
        return -1
    # Get left height
    left = binaryTreeDiameterHelper(tree.left, max_diameter)
    # Get right height
    right = binaryTreeDiameterHelper(tree.right, max_diameter)
    # Diameter at current node = left height + right height + 1 + 1
    # 2 is for counting left and right edge
    # if any of left or right is None, it will return -1 which will cancel the 1
    # then update max_height
    max_diameter[0] = max(max_diameter[0], left + right + 2)
    # return the max height to the previous node + 1
    return 1 + max(left, right)


class TestProgram():
    def test_case_1(self):
        root = BinaryTree(1)
        root.left = BinaryTree(3)
        root.left.left = BinaryTree(7)
        root.left.left.left = BinaryTree(8)
        root.left.left.left.left = BinaryTree(9)
        root.left.right = BinaryTree(4)
        root.left.right.right = BinaryTree(5)
        root.left.right.right.right = BinaryTree(6)
        root.right = BinaryTree(2)
        diameter = binaryTreeDiameter(root)
        print(diameter)


TestProgram().test_case_1()
