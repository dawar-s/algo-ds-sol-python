def productSum(array):
    s = 0
    for item in array:
        s += getSumHelper(item)
    return s


def getSumHelper(item, depth=1, s=0):
    if type(item) is int:
        return depth * item
    if type(item) is list:
        for i in item:
            s += depth * getSumHelper(i, depth + 1)
    return s
