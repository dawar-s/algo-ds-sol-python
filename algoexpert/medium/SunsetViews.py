def sunsetViews(buildings, direction):
    if direction == 'EAST':
        buildings = buildings[::-1]
    sunset = []
    max_height = float('-inf')
    for i, height in enumerate(buildings):
        if height > max_height:
            sunset.append(i)
            max_height = height

    if direction == 'EAST':
        sunset = sunset[::-1]
        sunset = [len(buildings) - 1 - val for val in sunset]

    return sunset


print(sunsetViews([3, 5, 4, 4, 3, 1, 3, 2], 'EAST'))
