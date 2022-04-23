def waterArea(heights):
    return calculate_area(heights, False) + calculate_area(heights[::-1], True)


def calculate_area(heights, right):
    i = 0
    area = 0
    while i < len(heights) and heights[i] == 0:
        i += 1
    if i == len(heights):
        return area
    while i < len(heights):
        j = i + 1
        pillar = 0
        steps = 0
        while j < len(heights) \
                and ((heights[j] < heights[i] and not right) or (heights[j] <= heights[i] and right)):
            pillar += heights[j]
            steps += 1
            j += 1
        if j == len(heights):
            break
        area += steps * heights[i] - pillar
        i = j
    return area


print(waterArea([0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]))
print(waterArea([0, 0, 0, 0, 0]))
print(waterArea([0, 1, 0, 0, 0]))
print(waterArea([0, 1, 2, 1, 1]))
print(waterArea([0, 1, 0, 1, 0, 2, 0, 3]))