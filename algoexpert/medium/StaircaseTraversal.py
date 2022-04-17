def staircaseTraversal(height, maxSteps):
    dp = [0 for _ in range(height + 1)]
    dp[0] = 1
    dp[1] = 1
    for i in range(2, len(dp)):
        j = i - 1
        tmp = maxSteps
        total = 0
        while tmp > 0 and j >= 0:
            total += dp[j]
            j -= 1
            tmp -= 1
        dp[i] = total
    print(dp)
    return dp[-1]


print(staircaseTraversal(10, 9))
