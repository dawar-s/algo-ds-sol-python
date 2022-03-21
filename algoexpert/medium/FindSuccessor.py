# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


# O(h) time, O(1) space where h is height of tree
def findSuccessor(tree, node):
    if node.right is not None:
        node = node.right
        while node.left is not None:
            node = node.left
        return node

    else:
        while node.parent is not None and node is node.parent.right:
            node = node.parent
        if node.parent is None:
            return None
        else:
            return node.parent
