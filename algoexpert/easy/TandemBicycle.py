def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort(reverse=fastest)
    s = 0
    for x, y in zip(redShirtSpeeds, blueShirtSpeeds):
        s += max(x, y)
    return s
