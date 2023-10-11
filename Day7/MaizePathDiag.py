def solution(n):
    def backtrack(r,c,dc):
        if r==n-1 and c==n-1:
            dc+=1
            return dc
        if r==n-1 or c==n-1:
            dc+=1
            return dc
        down = backtrack(r+1,c,dc)
        diag = backtrack(r+1,c+1,dc)
        right = backtrack(r,c+1,dc)
        return down+diag+right
    return backtrack(0,0,0)

def solutionPaths(n):
    def backtrack(s,r,c):
        if r==n-1 and c==n-1:
            res.append(s)
            return
        if r==n-1:
            s+='R'
            p = c
            while p!=n-2:
                s+='R'
                p+=1
            res.append(s)
            return
        if c==n-1:
            s+='D'
            p = r
            while p!=n-2:
                s+='D'
                p+=1
            res.append(s)
            return
        backtrack(s+'D',r+1,c)
        backtrack(s+'d',r+1,c+1)
        backtrack(s+'R',r,c+1)
        return res
    res = []
    return backtrack('',0,0)
n = int(input("Enter Matrix size = "))
print(solution(n))
# print(solutionPaths(n))