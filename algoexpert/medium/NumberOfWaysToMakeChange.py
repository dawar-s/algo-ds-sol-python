def numberOfWaysToMakeChange1(n, denoms):
    ways = [0]
    numberOfWaysToMakeChangeHelper(n, denoms, 0, 0, ways)
    return ways[0]

def numberOfWaysToMakeChangeHelper(n, denoms, idx, sum, ways):
    if idx >= len(denoms) or sum > n:
        return False
    if n == sum:
        return True

    i = idx
    while i < len(denoms):
        flag = numberOfWaysToMakeChangeHelper(n, denoms, i, sum + denoms[i], ways)
        if flag:
            ways[0] += 1
        i += 1

    return False

def numberOfWaysToMakeChange2(n, denoms):
    ways = [0 for _ in range(n+1)]
    ways[0] = 1
    for denom in denoms:
        for amount in range(1, n+1):
            if denom <= amount:
                ways[amount] += ways[amount - denom]

    return ways[n]


print(numberOfWaysToMakeChange2(25, [1, 5, 10, 25]))
