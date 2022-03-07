def selectionSort(array):
    i = 0
    while i < len(array):
        j = i
        k = j
        smallest = array[i]
        while j < len(array):
            if array[j] < smallest:
                smallest = array[j]
                k = j
            j += 1
        array[i], array[k] = array[k], array[i]
        i += 1
    return array
