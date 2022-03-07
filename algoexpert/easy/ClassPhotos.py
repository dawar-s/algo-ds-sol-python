def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()
    flag = redShirtHeights[0] > blueShirtHeights[0]
    for x, y in zip(redShirtHeights, blueShirtHeights):
        if (
            flag and y > x
        ) or (
            not flag and x > y
        ) or (
            x == y
        ):
            return False
    return True
