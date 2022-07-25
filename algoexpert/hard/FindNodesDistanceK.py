# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findNodesDistanceK(tree, target, k):
    path = []
    getPath(tree, target, path)
    for node in path:
        print(node.value)
    result = []
    target_node = path[0]
    getChildNodesDistanceK(target_node.left, k - 1, result)
    getChildNodesDistanceK(target_node.right, k - 1, result)
    getParentNodesDistanceK(path, k, result)
    print(result)


def getParentNodesDistanceK(path, k, result):
    for i in range(1, len(path)):
        if k == 0:
            break
        node = path[i]
        if node.left is path[i-1]:
            getChildNodesDistanceK(node.right, k, result)
        else:
            getChildNodesDistanceK(node.left, k, result)
        k -= 1


def getChildNodesDistanceK(node, k, result):
    if node is None:
        return
    if k == 0:
        result.append(node.value)
    getChildNodesDistanceK(node.left, k - 1, result)
    getChildNodesDistanceK(node.right, k - 1, result)


def getPath(tree, target, path):
    if tree is None:
        return False
    if tree.value == target:
        path.append(tree)
        return True
    left = getPath(tree.left, target, path)
    right = getPath(tree.right, target, path)
    if left or right:
        path.append(tree)
        return True
    return False




