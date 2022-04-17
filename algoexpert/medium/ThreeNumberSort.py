def threeNumberSort(array, order):
    if len(array) == 0:
        return []
    first = 0
    for num in order:
        second = first + 1
        while first < len(array):
            while first < len(array) and array[first] == num:
                first += 1
            if first == len(array):
                return array
            while second < len(array) and array[second] != num:
                second += 1
            if second == len(array):
                break
            if array[second] == num:
                swap(first, second, array)
            first += 1

    return array

def swap(x, y, array):
    array[x], array[y] = array[y], array[x]


print(threeNumberSort([-2, -3, -3, -3, -3, -3, -2, -2, -3], [-2, -3, 0]))
