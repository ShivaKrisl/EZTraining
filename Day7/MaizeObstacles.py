def findPaths(board):
    def backtrack(s,row,col):
        if row<n and col<n and board[row][col]==False:
            return
        if row==n-1 and col==n-1:
            res.append(s)
        if row==n-1:
            p = col
            while(p!=n-1):
                s+='R'
                p+=1
            res.append(s)
            return
        if col==n-1:
            p = row
            while(p!=n-1):
                s+='D'
                p+=1
            res.append(s)
            return
        backtrack(s+'D',row+1,col)
        backtrack(s+'d',row+1,col+1)
        backtrack(s+'R',row,col+1)
        return res
    res = []
    n = len(board)
    return backtrack("",0,0)

board = [
    [True,True,True],
    [True,False,True],
    [True,True,False]
    ]
print(*(findPaths(board)))
