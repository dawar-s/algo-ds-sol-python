def getPermutations(array):
    permutations = []
    helper(0, array, permutations)
    return permutations


def helper(i, array, permutations):
    if i == len(array) - 1:
        permutations.append(array[:])
        return
    for j in range(i, len(array)):
        swap(array, i, j)
        helper(i + 1, array, permutations)
        swap(array, i, j)


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


a = [1, 2, 3]
print(getPermutations(a))