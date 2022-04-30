def solveSudoku(board):
    helper(board, 0, 0)
    return board


def helper(board, row, col):
    if col == 9:
        row += 1
        if row == 9:
            return True
    col = col % 9

    if board[row][col] == 0:
        for digit in range(1, 10):
            if isValidValueInRow(board, row, col, digit) \
                    and isValidValueInCol(board, row, col, digit) \
                    and isValidValueInGrid(board, row, col, digit):
                board[row][col] = digit
                if not helper(board, row, col + 1):
                    board[row][col] = 0
                else:
                    return True

        return False

    return helper(board, row, col + 1)


def isValidValueInRow(board, row, col, value):
    for i in range(9):
        if i == col or board[row][i] == 0:
            continue
        if board[row][i] == value:
            return False
    return True


def isValidValueInCol(board, row, col, value):
    for i in range(9):
        if i == row or board[i][col] == 0:
            continue
        if board[i][col] == value:
            return False
    return True


def isValidValueInGrid(board, row, col, value):
    row_start = row - row % 3
    row_end = row_start + 3
    col_start = col - col % 3
    col_end = col_start + 3
    for i in range(row_start, row_end):
        for j in range(col_start, col_end):
            if (i == row and j == col) or board[i][j] == 0:
                continue
            if board[i][j] == value:
                return False
    return True


a = [
    [0, 0, 0, 0, 3, 0, 0, 0, 9],
    [0, 4, 0, 5, 0, 0, 0, 7, 8],
    [2, 9, 0, 0, 0, 1, 0, 5, 0],
    [0, 7, 8, 0, 0, 3, 0, 0, 6],
    [0, 3, 0, 0, 6, 0, 0, 8, 0],
    [6, 0, 0, 8, 0, 0, 9, 3, 0],
    [0, 6, 0, 9, 0, 0, 0, 2, 7],
    [7, 2, 0, 0, 0, 5, 0, 6, 0],
    [8, 0, 0, 0, 7, 0, 0, 0, 0]
]


def printSudokuBoard(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print('\n', '-' * 21, sep='')
        else:
            print('')
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print('|', end=' ')
            print('-' if board[i][j] == 0 else board[i][j], end=' ')


printSudokuBoard(a)
print('\n')
printSudokuBoard(solveSudoku(a))
