# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, rootidx):
        self.rootidx = rootidx


# O(n) time | O(n) space
def reconstructBst(preOrderTraversalValues):
    treeinfo = TreeInfo(0)
    return helper(preOrderTraversalValues, treeinfo, float('-inf'), float('inf'))


def helper(preOrderTraversalValues, treeinfo, lower, upper):
    if treeinfo.rootidx == len(preOrderTraversalValues):
        return None
    value = preOrderTraversalValues[treeinfo.rootidx]
    if value < lower or value >= upper:
        return None
    treeinfo.rootidx += 1
    left = helper(preOrderTraversalValues, treeinfo, lower, value)
    right = helper(preOrderTraversalValues, treeinfo, value, upper)
    return BST(value, left, right)
