def zigzagTraverse(array):
    result = []
    down = True
    row, col = 0, 0
    while True:
        result.append(array[row][col])
        if down:
            if row_col_in_bound(row + 1, col - 1, array):
                row += 1
                col -= 1
            elif row_in_bound(row + 1, array):
                row += 1
                down = False
            elif col_in_bound(col + 1, array):
                col += 1
                down = False
            else:
                break
        else:
            if row_col_in_bound(row - 1, col + 1, array):
                row -= 1
                col += 1
            elif col_in_bound(col + 1, array):
                col += 1
                down = True
            elif row_in_bound(row + 1, array):
                row += 1
                down = True
            else:
                break

    return result


def row_col_in_bound(row, col, array):
    return row_in_bound(row, array) and col_in_bound(col, array)


def row_in_bound(row, array):
    return -1 < row < len(array)


def col_in_bound(col, array):
    return -1 < col < len(array[0])


a = [
    [1, 3, 4, 10, 11],
    [2, 5, 9, 12, 20],
    [6, 8, 13, 19, 21],
    [7, 14, 18, 22, 27],
    [15, 17, 23, 26, 28],
    [16, 24, 25, 29, 30]
  ]
print(zigzagTraverse(a))
