def solution(n):
    def backtrack(r,c,dc):
        if r==n-1 or c==n-1:
            dc+=1
            return dc
        down = backtrack(r+1,c,dc)
        right = backtrack(r,c+1,dc)
        return down+right

    return backtrack(0,0,dc)

def solutionPrintPaths(n):
    def backtrack(s,r,c):
        if r==n-1:
            s+='R'
            p = c
            while(p!=n-2):
                s+='R'
                p+=1
            res.append(s)
            return
        if c==n-1:
            s+='D'
            p = r
            while(p!=n-2):
                s+='D'
                p+=1
            res.append(s)
            return
        backtrack(s+'D',r+1,c)
        backtrack(s+'R',r,c+1)
        return res
    return backtrack('',0,0) 
n = int(input("Enter matrix size = "))
res = []
dc=0
#print(solution(n))
print(solutionPrintPaths(n))