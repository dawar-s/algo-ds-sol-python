def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    i = j = 0
    arr = [arrayOne[0], arrayTwo[0]]
    while i < len(arrayOne) and j < len(arrayTwo):
        if get_absolute_diff(arrayOne[i], arrayTwo[j]) < abs(arr[0] - arr[1]):
            arr[0], arr[1] = arrayOne[i], arrayTwo[j]
        if arrayOne[i] <= arrayTwo[j]:
            i += 1
        else:
            j += 1

    return arr


def get_absolute_diff(a, b):
    return max(a, b) - min(a, b)
