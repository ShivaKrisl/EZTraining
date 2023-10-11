def BS(n,start,end):
    mid = start+(end-start)/2
    if int(mid*mid) == n:
        return (mid)
    if int(mid*mid)<n:
        return BS(n,mid+1,end)
    if int(mid*mid)>n:
        return BS(n,start,mid-1)
n = int(input())
print(BS(n,1,n//2))