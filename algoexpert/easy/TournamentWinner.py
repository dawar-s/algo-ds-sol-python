def tournamentWinner(competitions, results):
    dic = {}
    for i, c in enumerate(competitions):
        dic[c[results[i] ^ 1]] = dic.get(c[results[i] ^ 1], 0) + 3

    return max(dic, key=dic.get)
