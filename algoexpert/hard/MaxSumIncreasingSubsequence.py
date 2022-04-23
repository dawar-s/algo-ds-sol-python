def maxSumIncreasingSubsequence(array):
    sequence = [[] for _ in array]
    sequence[0] = [array[0]]
    if len(array) == 1:
        return [array[0], [array[0]]]
    max_sum = array[:]
    global_max = array[0]
    global_max_id = 0
    for i in range(1, len(array)):
        current_max = max_sum[i]
        lst = [current_max]
        for j in range(i):
            if array[i] > array[j] and array[i] + max_sum[j] > current_max:
                current_max = array[i] + max_sum[j]
                lst = sequence[j] + [array[i]]
            max_sum[i] = current_max
            sequence[i] = lst
        if current_max > global_max:
            global_max = current_max
            global_max_id = i

    return [max_sum[global_max_id], sequence[global_max_id]]


print(maxSumIncreasingSubsequence([8, 12, 2, 3, 15, 5, 7]))
print(maxSumIncreasingSubsequence([10, 70, 20, 30, 50, 11, 30]))
print(maxSumIncreasingSubsequence([-1, 1]))
print(maxSumIncreasingSubsequence([5, 4, 3, 2, 1]))
print(maxSumIncreasingSubsequence([-5, -4, -3, -2, -1]))
print(maxSumIncreasingSubsequence([10, 15, 4, 5, 11, 14, 31, 25, 31, 23, 25, 31, 50]))
