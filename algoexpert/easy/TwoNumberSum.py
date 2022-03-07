def twoNumberSum(array, targetSum):
    arr = []

    if len(array) < 2:
        return arr

    for i in range(len(array)):
        for j in range(len(array)):
            if i != j and array[i] + array[j] == targetSum:
                arr = [array[i], array[j]]
                return arr

    return arr
