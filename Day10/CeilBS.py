def BS(l,start,end,se):
    mid = start+(end-start)//2
    if se == l[mid]:
        return l[mid]
    if start>end:
        return -1
    if start==end:
        return l[start]
    if se<l[mid]:
        return BS(l,start,mid,se)
    if se>l[mid]:
        return BS(l,mid+1,end,se)
    
l = list(map(int,input().split()))
se = int(input())
print(BS(l,0,len(l)-1,se))