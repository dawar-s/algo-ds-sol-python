# O(m*n) time | O(m*n) space
def riverSizes(matrix):
    row = len(matrix)
    column = len(matrix[0])
    visited = [[False] * column for _ in range(row)]
    queue = []
    result = []

    for i in range(row):
        for j in range(column):
            queue.append([i, j, matrix[i][j]])
            length = 0
            while len(queue) > 0:
                x, y, val = queue.pop(0)
                if val == 1 and not visited[x][y]:
                    length += 1
                    visited[x][y] = True
                    if x > 0 and not visited[x - 1][y]:
                        queue.append([x - 1, y, matrix[x - 1][y]])
                    if x < row - 1 and not visited[x + 1][y]:
                        queue.append([x + 1, y, matrix[x + 1][y]])
                    if y > 0 and not visited[x][y - 1]:
                        queue.append([x, y - 1, matrix[x][y - 1]])
                    if y < column - 1 and not visited[x][y + 1]:
                        queue.append([x, y + 1, matrix[x][y + 1]])

            if length > 0:
                result.append(length)

    return result
