def maxSubsetSumNoAdjacent(array):
    if not array:
        return 0
    if len(array) == 1:
        return array[0]

    max_array = array[:]
    max_array[1] = max(max_array[0], max_array[1])
    for i in range(2, len(array)):
        max_array[i] = max(max_array[i-1], max_array[i-2] + array[i])

    return max_array[-1]


a = [75, 105, 120, 70, 90, 135]
print(maxSubsetSumNoAdjacent(a))
