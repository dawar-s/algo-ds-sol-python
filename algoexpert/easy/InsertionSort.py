def insertionSort(array):
    end = 0
    while end < len(array) - 1:
        i = end
        while i >= 0 and array[i+1] < array[i]:
            array[i+1], array[i] = array[i], array[i+1]
            i -= 1
        end += 1
    return array
