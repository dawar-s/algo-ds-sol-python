def minHeightBst(array):
    mid = len(array) // 2
    root = BST(array[mid])
    minHeightBstHelper(array, root, 0, mid - 1)
    minHeightBstHelper(array, root, mid + 1, len(array) - 1)
    return root


def minHeightBstHelper(array, tree, start, end):
    if start > end:
        return
    mid = (start + end) // 2
    tree.insert(array[mid])
    minHeightBstHelper(array, tree, start, mid - 1)
    minHeightBstHelper(array, tree, mid + 1, end)


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
