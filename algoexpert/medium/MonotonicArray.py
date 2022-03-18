def isMonotonic(array):
    is_increasing = True
    is_decreasing = True

    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            is_increasing = False
        elif array[i] > array[i - 1]:
            is_decreasing = False

    return is_increasing or is_decreasing

