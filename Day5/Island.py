def pathfinder(mat,i,j):
    if i<0 or j<0 or i>=len(mat) or j>=len(mat) or mat[i][j]==0:
        return 
    mat[i][j] = 0
    pathfinder(mat,i,j+1)
    pathfinder(mat,i,j-1)
    pathfinder(mat,i+1,j)
    pathfinder(mat,i-1,j)
mat = [[1,0,0,1],[1,0,1,0],[0,1,0,1],[1,0,1,1]]
dc=0
for i in range(len(mat)):
    for j in range(len(mat)):
        if mat[i][j]==1:
            dc+=1
            pathfinder(mat,i,j)
print(dc)