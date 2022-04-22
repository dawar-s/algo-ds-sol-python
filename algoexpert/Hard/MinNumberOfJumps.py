def minNumberOfJumps(array):
    return helper(0, array, 0)


def helper(current_idx, array, current_jumps):
    if current_idx >= len(array) - 1:
        return current_jumps

    min_array = []
    for i in range(1, array[current_idx] + 1):
        jumps = helper(current_idx + i, array, current_jumps + 1)
        min_array.append(jumps)

    return min(min_array)


def minNumberOfJumps2(array):
    dp = [float('inf') for _ in array]
    dp[0] = 0
    for i in range(1, len(array)):
        for j in range(i):
            if j + array[j] < i:
                continue
            dp[i] = min(dp[i], dp[j] + 1)

    return dp[-1]


print(minNumberOfJumps2([1, 1]))