def removeIslands(matrix):
    h = len(matrix)
    w = len(matrix[0])
    visited = [[0 for _ in range(w)] for _ in range(h)]
    for row in range(h):
        for col in range(w):
            if row == 0 \
                    or row == h - 1 \
                    or col == 0 \
                    or col == w - 1:
                dfs(matrix, visited, [], row, col, h, w)

    return visited


def dfs(matrix, visited, stack, row, col, h, w):
    if 0 <= row < h and 0 <= col < w and matrix[row][col] == 1 and visited[row][col] == 0:
        stack.append([row, col])
        while stack:
            item = stack.pop(-1)
            row = item[0]
            col = item[1]
            visited[row][col] = 1
            dfs(matrix, visited, stack, row - 1, col, h, w)
            dfs(matrix, visited, stack, row + 1, col, h, w)
            dfs(matrix, visited, stack, row, col - 1, h, w)
            dfs(matrix, visited, stack, row, col + 1, h, w)


matrix = \
    [
        [1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 1],
        [0, 0, 1, 0, 1, 0],
        [1, 1, 0, 0, 1, 0],
        [1, 0, 1, 1, 0, 0],
        [1, 0, 0, 0, 0, 1]
    ]

print(removeIslands(matrix))
