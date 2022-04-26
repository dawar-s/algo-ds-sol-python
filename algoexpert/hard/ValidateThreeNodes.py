# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    a = isDescendant(nodeOne, nodeTwo) and isDescendant(nodeTwo, nodeThree)
    b = isDescendant(nodeTwo, nodeOne) and isDescendant(nodeThree, nodeTwo)
    return a or b


def isDescendant(node1, node2):
    """
    Checks if node1 is descendant of node2

    :param node1:
    :param node2:
    :return: True if node1 is descendant of node2, False otherwise
    """
    if node2 is None:
        return False
    if node1 is node2:
        return True
    return isDescendant(node1, node2.left) if node1.value < node2.value else isDescendant(node1, node2.right)


root = BST(5)

root.left = BST(2)
root.left.left = BST(1)
root.left.right = BST(4)
root.left.left.left = BST(0)
root.left.right.left = BST(3)

root.right = BST(7)
root.right.left = BST(6)
root.right.right = BST(8)

print(validateThreeNodes(root, root.left, root.left.right.left))

