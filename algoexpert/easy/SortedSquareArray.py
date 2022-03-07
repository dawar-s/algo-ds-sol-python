# O(n) time | O(n) space, where n is length of array
def sortedSquaredArray(array):
    if len(array) < 2:
        return [array[0] ** 2]

    i, j, k = 0, len(array) - 1, len(array) - 1
    arr = [0] * len(array)
    while True:
        if i == j:
            arr[k] = array[i] ** 2
            break
        elif abs(array[i]) >= abs(array[j]):
            arr[k] = array[i] ** 2
            i += 1
        elif abs(array[i]) < abs(array[j]):
            arr[k] = array[j] ** 2
            j -= 1
        k -= 1

    return arr
