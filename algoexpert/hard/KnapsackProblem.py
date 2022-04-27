def knapsackProblem(items, capacity):
    dp = [[0 for _ in range(capacity + 1)] for _ in range(len(items) + 1)]
    for i in range(1, len(dp)):
        value = items[i - 1][0]
        weight = items[i - 1][1]
        for j in range(len(dp[0])):
            if weight > j:
                dp[i][j] = dp[i-1][j]
                continue
            dp[i][j] = max(value + dp[i-1][j-weight], dp[i-1][j])

    included_items = traceItems(dp, items)

    return [dp[-1][-1], included_items]


def traceItems(dp, items):
    row, col = len(dp) - 1, len(dp[0]) - 1
    included_items = []
    while row >= 1 and col >= 1:
        if dp[row][col] != dp[row-1][col]:
            included_items.append(row-1)
            col -= items[row - 1][1]
            row -= 1
        else:
            row -= 1

    return included_items
