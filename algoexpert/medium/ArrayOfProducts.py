def arrayOfProducts(array):
    left = [1] * len(array)
    right = [1] * len(array)

    for i in range(1, len(array)):
        left[i] = left[i-1] * array[i-1]

    for i in range(len(array)-2, -1, -1):
        right[i] = right[i+1] * array[i+1]

    return [a * b for a, b in zip(left, right)]
