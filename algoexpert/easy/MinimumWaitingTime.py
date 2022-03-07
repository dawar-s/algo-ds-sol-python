def minimumWaitingTime(queries):
    if len(queries) == 1:
        return 0
    queries.sort()
    queries.pop()
    prev = 0
    s = 0
    for num in queries:
        c = num + prev
        s += c
        prev = c
    return s
