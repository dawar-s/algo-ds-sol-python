# O(n) time | O(n) space
def kadanesAlgorithm1(array):
    if len(array) == 0:
        return 0
    max_sum = [float('-inf') for _ in array]
    max_sum[0] = array[0]
    for i in range(1, len(array)):
        max_sum[i] = max(array[i], max_sum[i-1] + array[i])

    return max(max_sum)


# O(n) time | O(1) space
def kadanesAlgorithm2(array):
    if len(array) == 0:
        return 0
    prev, max_sum = array[0], array[0]
    for i in range(1, len(array)):
        current = max(array[i], prev + array[i])
        prev = current
        max_sum = max(current, max_sum)

    return max_sum
