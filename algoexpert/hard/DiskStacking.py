def diskStacking(disks: list):
    disks.sort(key=lambda x: x[2])
    heights = [disk[2] for disk in disks]
    sequences = [None for _ in disks]
    maxHeightIdx = 0
    for i in range(1, len(disks)):
        current = disks[i]
        for j in range(i):
            previous = disks[j]
            if areValidDimensions(previous, current):
                if heights[i] <= current[2] + heights[j]:
                    heights[i] = current[2] + heights[j]
                    sequences[i] = j
        if heights[i] >= heights[maxHeightIdx]:
            maxHeightIdx = i

    result = []
    while maxHeightIdx is not None:
        result.append(disks[maxHeightIdx])
        maxHeightIdx = sequences[maxHeightIdx]

    return list(reversed(result))


def areValidDimensions(previous, current):
    return previous[0] < current[0] \
           and previous[1] < current[1] \
           and previous[2] < current[2]


a = [[2, 1, 2],
    [3, 2, 3],
    [2, 2, 8],
    [2, 3, 4],
    [1, 3, 1],
    [4, 4, 5]]
print(diskStacking(a))