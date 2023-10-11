def printer(l,n,c,i,j):
    if c>n*n:
        return l
    if i<0 and j==n:
        i=0
        j = n-2
    else:
        if i<0:
            i = n-1
        if j==n:
            j = 0
    if l[i][j]!=0:
        i = i+1
        j = j-2
        printer(l,n,c,i,j)
    l[i][j] = c
    printer(l,n,c+1,i-1,j+1)
    return l
    
n = int(input())
l = [[0 for j in range(n)]for i in range(n)]
l[n//2][n-1] = 1
i = n//2
j = n-1
print(*(printer(l,n,2,i-1,j+1)))