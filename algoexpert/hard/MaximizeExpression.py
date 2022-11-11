def maximizeExpression(array):
    if len(array) < 4:
        return 0

    dp = [[float('-inf') for x in array] for y in range(4)]

    for i in range(4):
        for j in range(i, len(array) - 3 + i):
            if i == 0 and j == 0:
                dp[0][0] = array[0]
            elif i == 0:
                dp[i][j] = max(dp[i][j - 1], array[j])
            elif i == 1 or i == 3:
                dp[i][j] = max(dp[i - 1][j - 1] - array[j], dp[i][j - 1])
            elif i == 2:
                dp[i][j] = max(dp[i - 1][j - 1] + array[j], dp[i][j - 1])

    return dp[-1][-1]
