def minNumberOfCoinsForChange(n, denoms):
    if n == 0:
        return 0

    ways = [i // denoms[0] if i % denoms[0] == 0 else float('inf') for i in range(n + 1)]

    for denom in denoms[1:]:
        for i in range(n + 1):
            if denom == i:
                ways[i] = 1
            elif denom < i and ways[i - denom] != float('inf'):
                ways[i] = min(ways[i], 1 + ways[i - denom])

    return ways[n] if ways[n] != float('inf') else -1


array = [
    [7, [1, 5, 10]],
    [7, [1, 10, 5]],
    [7, [10, 1, 5]],
    [0, [1, 2, 3]],
    [3, [2, 1]],
    [4, [1, 5, 10]],
    [10, [1, 5, 10]],
    [11, [1, 5, 10]],
    [24, [1, 5, 10]],
    [25, [1, 5, 10]]
]

for item in array:
    print(f'Change:{item[0]}, '
          f'Denomination: {item[1]}, '
          f'Min number of coins for change: {minNumberOfCoinsForChange(item[0], item[1])}')
