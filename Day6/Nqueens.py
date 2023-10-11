def is_valid(board, row, col, n):
    for i in range(col):# check horizontal
        if board[row][i] == 1:
            return False
    i = row
    j = col
    while i>=0 and j >= 0: # upper left diag
        if board[i][j] == 1:
            return False
        i -= 1 
        j -= 1 
    i = row
    j = col
    while i<n and j >=0: #bottom left diag
        if board[i][j] == 1:
            return False
        i += 1 
        j -= 1
    return True
def solve(n):
    board = [[0 for i in range(n)] for j in range(n)]
    def backtrack(col):
        if col == n:
            return True
        for i in range(n):
            if is_valid(board, i, col, n):
                board[i][col] = 1
                if backtrack(col+1):
                    return True
                board[i][col] = 0
        return False
    if backtrack(0):

        for row in board:

            print(row)
    else:
        print("no solution")
n = 9
if n<=0:
    print("no solution")
else:
    solve(n)