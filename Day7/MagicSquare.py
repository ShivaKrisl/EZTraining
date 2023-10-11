def fillmat(n):
    l = [[0 for j in range(n)]for i in range(n)]
    i = n//2
    j = n-1
    c =1
    while c<=n*n:
        if i<0 and j==n:
            i = 0
            j = n-2
        else:
            if i<0:
                i = n-1
            if j==n:
                j=0
        if l[i][j]!=0:
            i = i+1
            j = j-2
            continue
        l[i][j] = c
        c+=1
        i=i-1
        j = j+1
    return l
n = int(input("Enter Odd num = "))
print(*(fillmat(n)))
