def minRewards(scores):
    awards = [1 for _ in scores]
    for i in range(1, len(scores)):
        if scores[i] > scores[i - 1]:
            awards[i] = awards[i - 1] + 1

    for i in range(len(scores) - 2, -1, -1):
        if scores[i] > scores[i + 1]:
            awards[i] = max(awards[i], awards[i + 1] + 1)

    return sum(awards)


print(minRewards([800, 400, 20, 10, 30, 61, 70, 90, 17, 21, 22, 13, 12, 11, 8, 4, 2, 1, 3, 6, 7, 9, 0, 68, 55, 67, 57,
                  60, 51, 661, 50, 65, 53]))

