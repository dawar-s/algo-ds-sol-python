def maximumSumSubmatrix(matrix, size):
    max_sum = float('-inf')
    h, w = len(matrix), len(matrix[0])
    dp = [[0 for _ in range(w+1)] for _ in range(h+1)]
    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            dp[i][j] = matrix[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
    max_sum = float('-inf')
    for i in range(size, len(dp)):
        for j in range(size, len(dp[0])):
            max_sum = max(max_sum, (dp[i][j] - dp[i-size][j] - dp[i][j-size] + dp[i-size][j-size]))
    return max_sum