def threeNumberSum(array, targetSum):
    current = 0
    result = []
    array.sort()
    while current < len(array) - 1:
        left = current + 1
        right = len(array) - 1
        while left < right:
            if (s := array[left] + array[current] + array[right]) == targetSum:
                result.append([array[current], array[left], array[right]])
                left += 1
                right -= 1
            elif s < targetSum:
                left += 1
            else:
                right -= 1
        current += 1

    return result
