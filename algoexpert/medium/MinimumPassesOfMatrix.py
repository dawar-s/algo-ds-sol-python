from collections import deque

def minimumPassesOfMatrix(matrix: list):
    queue = deque()
    r = len(matrix)
    c = len(matrix[0])
    for row in range(r):
        for col in range(c):
            if matrix[row][col] > 0:
                queue.append([row, col])

    if len(queue) == r * c:
        return 0

    passes = 0
    while True:
        lst = []
        while queue:
            row, col = queue.popleft()
            add_to_list(row, col, lst, matrix)

        if len(lst) > 0:
            passes += 1
            for item in lst:
                queue.append(item)
        else:
            break

    for row in range(r):
        for col in range(c):
            if matrix[row][col] < 0:
                return -1

    return passes


def add_to_list(row, col, lst, matrix):
    if row-1 >= 0 and matrix[row-1][col] < 0:
        matrix[row-1][col] *= -1
        lst.append([row-1, col])
    if row+1 < len(matrix) and matrix[row+1][col] < 0:
        matrix[row+1][col] *= -1
        lst.append([row+1, col])
    if col+1 < len(matrix[0]) and matrix[row][col+1] < 0:
        matrix[row][col+1] *= -1
        lst.append([row, col+1])
    if col-1 >= 0 and matrix[row][col-1] < 0:
        matrix[row][col-1] *= -1
        lst.append([row, col-1])



m = [
    [1, 0, 0, -2, -3],
    [-4, -5, -6, -2, -1],
    [0, 0, 0, 0, -1],
    [-1, 0, 3, 0, 3]
  ]

print(minimumPassesOfMatrix(m))