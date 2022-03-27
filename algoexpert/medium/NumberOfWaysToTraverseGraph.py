def numberOfWaysToTraverseGraph(width, height, memo=None, row=0, col=0):
    if row == height - 1 and col == width - 1:
        return 1
    if row == height or col == width:
        return 0
    if memo is None:
        memo = {}
    key = str(row) + ',' + str(col)
    if key in memo:
        return memo[key]

    memo[key] = numberOfWaysToTraverseGraph(width, height, memo, row + 1, col) + \
                numberOfWaysToTraverseGraph(width, height, memo, row, col + 1)

    return memo[key]


print(numberOfWaysToTraverseGraph(3, 2))
