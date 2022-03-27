def numberOfWaysToTraverseGraph(width, height, memo=None):
    if height == 1 or width == 1:
        return 1
    if memo is None:
        memo = {}
    key = str(height) + ',' + str(width)
    if key in memo:
        return memo[key]

    memo[key] = numberOfWaysToTraverseGraph(width - 1, height, memo) + \
                numberOfWaysToTraverseGraph(width, height - 1, memo)

    return memo[key]


print(numberOfWaysToTraverseGraph(10, 10))
