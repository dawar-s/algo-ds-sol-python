def bubbleSort(array):
    start = 0
    end = len(array) - 1
    swap = True
    while swap:
        swap = False
        i, j = 0, 1
        while j <= end:
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
                swap = True
            i += 1
            j += 1
        end -= 1

    return array
