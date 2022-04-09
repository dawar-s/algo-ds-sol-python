def cycleInGraph(edges):
    visited = [False for _ in edges]
    stack = [False for _ in edges]
    for node in range(len(edges)):
        if visited[node]:
            continue
        has_cycle = dfs(edges, node, visited, stack)
        if has_cycle:
            return True
    return False


def dfs(edges, node, visited, stack):
    if stack[node]:
        return True
    if visited[node]:
        return False
    if not visited[node]:
        visited[node] = True
        stack[node] = True
    for neighbors in edges[node]:
        flag = dfs(edges, neighbors, visited, stack)
        if flag:
            return True
    stack[node] = False
    return False
