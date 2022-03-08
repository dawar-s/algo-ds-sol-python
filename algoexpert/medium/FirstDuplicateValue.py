def firstDuplicateValue(array):
    for n in array:
        n = abs(n)
        if array[n - 1] < 0:
            return n
        array[n - 1] *= -1
    return -1
