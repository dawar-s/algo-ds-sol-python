# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree, min_value=float('-inf'), max_value=float('inf')):
    if tree is None:
        return True
    if min_value <= tree.value < max_value:
        return validateBst(tree.left, min_value, tree.value) and \
               validateBst(tree.right, tree.value, max_value)
    return False
