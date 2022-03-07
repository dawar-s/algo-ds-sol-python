def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, tree.value)


def findClosestValueInBstHelper(tree, target, closest_val):
    if tree is None:
        return closest_val
    if abs(tree.value - target) < abs(closest_val - target):
        closest_val = tree.value
    if tree.value < target:
        return findClosestValueInBstHelper(tree.right, target, closest_val)
    elif tree.value > target:
        return findClosestValueInBstHelper(tree.left, target, closest_val)
    else:
        return closest_val


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
