def spiralTraverse(array):
    start_row, end_row = 0, len(array)
    start_col, end_col = 0, len(array[0])
    result = []
    while start_row < end_row and start_col < end_col:

        result.extend([array[start_row][x] for x in range(start_col, end_col)])

        result.extend([array[x][end_col - 1] for x in range(start_row + 1, end_row - 1)])

        if start_row == end_row - 1:
            break
        result.extend([array[end_row - 1][x] for x in reversed(range(start_col, end_col))])

        if start_col == end_col - 1:
            break
        result.extend([array[x][start_col] for x in reversed(range(start_row + 1, end_row - 1))])

        start_row += 1
        end_row -= 1
        start_col += 1
        end_col -= 1

    return result
