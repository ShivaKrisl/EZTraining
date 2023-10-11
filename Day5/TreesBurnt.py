import time as t
def pathfinder(mat,i,j):
    if i<0 or j<0 or i>=len(mat) or j>=len(mat) or mat[i][j]==0:
        return 
    mat[i][j]=0
    pathfinder(mat,i,j+1)
    pathfinder(mat,i,j-1)
    pathfinder(mat,i+1,j)
    pathfinder(mat,i-1,j)

mat = [[1,0,0,1],[1,0,0,0],[1,0,1,0],[0,1,1,1]]
x,y = map(int,input().split())
s = t.time()
pathfinder(mat,x,y)
print(mat)
dc=0
for i in range(len(mat)):
    dc+=mat[i].count(1)
e = t.time()
print(dc)
print(s)
