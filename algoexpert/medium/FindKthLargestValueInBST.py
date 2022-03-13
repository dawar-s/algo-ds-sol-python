# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    info = [0, 0]  # info[0] = number of visited nodes, info[1] = value of the last node
    findKthLargestValueInBstHelper(tree, k, info)
    return info[1]


def findKthLargestValueInBstHelper(tree, k, info=[0, 0]):
    if tree is None or info[0] >= k:
        return
    findKthLargestValueInBstHelper(tree.right, k, info)
    if info[0] < k:
        info[0] += 1
        info[1] = tree.value
        findKthLargestValueInBstHelper(tree.left, k, info)


class TestProgram:
    def test_case_1(self):
        root = BST(15)
        root.left = BST(5)
        root.left.left = BST(2)
        root.left.left.left = BST(1)
        root.left.left.right = BST(3)
        root.left.right = BST(5)
        root.right = BST(20)
        root.right.left = BST(17)
        root.right.right = BST(22)
        k = 3
        expected = 17
        actual = findKthLargestValueInBst(root, k)
        print(actual)


TestProgram().test_case_1()
