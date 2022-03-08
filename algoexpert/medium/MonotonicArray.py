def isMonotonic(array):
    isIncreasing = True
    isDecreasing = True

    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            isIncreasing = False
        elif array[i] > array[i - 1]:
            isDecreasing = False

    return isIncreasing or isDecreasing

