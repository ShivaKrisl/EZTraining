# I can move in all 4 directions L,R,U,D
def findAll(board):
    def backtrack(s,row,col):
        if row==n-1:
            p = col
            while p!=n-1:
                s+='R'
                p+=1
            res.append(s)
            board[row][col] = False
            return
        if col==n-1:
            p = row
            while p!=n-1:
                s+='D'
                p+=1
            res.append(s)
            board[row][col] = False
            return
        if row<0 or col<0 or row>n-1 or col>n-1 or board[row][col]==False:
            return 
        board[row][col] = False
        if row<n-1:
            backtrack(s+'D',row+1,col)
            # board[row][col] = True
        if col<n-1:
            backtrack(s+'R',row,col+1)
        if row>0:
            backtrack(s+'U',row-1,col)
        if col>0:
            backtrack(s+'L',row,col-1)
        board[row][col] = True
        return res 
    res = []
    n = len(board)
    return backtrack('',0,0)

board = [
    [True,True,True],
    [True,True,True],
    [True,True,True]
]
print(*(findAll(board)))
    