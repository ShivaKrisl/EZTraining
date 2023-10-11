class Solution:
    def solveNQueens(self, n: int):
        res = []
        col = []
        pos = []
        neg = []
        board = [['.']*(n) for i in range(n)]
        def back(r):
            if r==n:
                return True
            for c in range(n):
                if c in col or (r+c) in pos or (r-c) in neg:
                    continue
                board[r][c] = 'Q'
                col.append(c)
                pos.append(r+c)
                neg.append(r-c)
                back(r+1)
                board[r][c]='.'
                col.remove(c)
                pos.remove(r+c)
                neg.remove(r-c)
        back(0)
        return res
