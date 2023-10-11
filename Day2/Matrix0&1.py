import numpy as np
def horizontal(l,n):
    for i in range(len(l)):
        if l[i]!=n:
            return 0
    return 1
n=4
mat = list()
for i in range(n):
    a = []
    for j in range(n):
        a.append(int(input()))
    mat.append(a)

for i in range(n):
    for j in range(n):
        print(mat[i][j],end=" ")
    print()
    
dc_1 = 0
dc_0 = 0
for i in range(n):
    dc_1+=horizontal(mat[i],1)
    dc_0+=horizontal(mat[i],0)
print("Horizontal 1's = ",dc_1)
print("Horizontal 0's = ",dc_0)


# diagonal
dc_rdiag_1 = 0
dc_rdiag_0 = 0
dc_ldiag_1 = 0
dc_ldiag_0 = 0
for i in range(n):
    for j in range(n):
        if i==j and mat[i][j]==1:
            dc_rdiag_1+=1
        elif i==j and mat[i][j]==0:
            dc_rdiag_0+=1
        elif i+j==n-1:
            if mat[i][j]==1:
                dc_ldiag_1 += 1
            elif mat[i][j]==0:
                dc_ldiag_0+=1
print("left diagonal 1's = ",dc_rdiag_1//n)
print("left diagonal 0's = ",dc_rdiag_0//n)
print("right diagonal 1s = ",dc_ldiag_1//n)
print("right diagonal 0s = ",dc_ldiag_0//n)


# vertical
t = [[]]
t = np.array(mat)
t = t.T
dc_1 = 0
dc_0 = 0
for i in range(n):
    dc_1+=horizontal(t[i],1)
    dc_0+=horizontal(t[i],0)
print("Vertical 1's = ",dc_1)  
print("Vertical 0's = ",dc_0)