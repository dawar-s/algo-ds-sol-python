# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def evaluateExpressionTree(tree):
    op_map = {
        -1: lambda x, y: x + y,
        -2: lambda x, y: x - y,
        -3: lambda x, y: int(x / y),
        -4: lambda x, y: x * y
    }
    return evaluateExpressionTreeHelper(tree, op_map)


def evaluateExpressionTreeHelper(node, op_map):
    if node.value >= 0:
        return node.value
    return op_map[node.value](evaluateExpressionTreeHelper(node.left, op_map),
                              evaluateExpressionTreeHelper(node.right, op_map))
