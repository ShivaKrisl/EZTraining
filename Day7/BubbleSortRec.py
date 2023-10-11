def swapper(l,i,j,n):
    if n==1:
        return
    if j==n:
        i=0
        j=1
        n = n-1
    if l[i]>l[j]:
        l[i],l[j] = l[j],l[i]
    swapper(l,i+1,j+1,n)
l = list(map(int,input().split()))
swapper(l,0,1,len(l))
print(l)