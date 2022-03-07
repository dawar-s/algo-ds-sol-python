def moveElementToEnd(array, toMove):
    i = len(array) - 1
    while i > -1 and array[i] == toMove:
        i -= 1
    if i <= 0:
        return array
    j = i - 1
    while j >= 0:
        if array[j] == toMove:
            array[i], array[j] = array[j], array[i]
            i -= 1
        j -= 1

    return array
