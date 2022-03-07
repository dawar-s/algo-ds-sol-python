def nonConstructibleChange(coins):
    if len(coins) == 0:
        return 1
    coins.sort()
    change = 0
    for coin in coins:
        if coin > change + 1:
            return change + 1
        change += coin

    return change + 1