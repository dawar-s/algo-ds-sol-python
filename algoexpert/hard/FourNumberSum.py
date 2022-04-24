def fourNumberSum(array, targetSum):
    allPairSum = {}
    quadruplets = []
    for i in range(1, len(array) - 1):
        for j in range(i + 1, len(array)):
            current_sum = array[i] + array[j]
            diff = targetSum - current_sum
            if diff in allPairSum:
                for pair in allPairSum[diff]:
                    quadruplets.append(pair + [array[i], array[j]])
        for k in range(0, i):
            current_sum = array[i] + array[k]
            if current_sum not in allPairSum:
                allPairSum[current_sum] = [[array[k], array[i]]]
            else:
                allPairSum[current_sum].append([array[k], array[i]])

    return quadruplets