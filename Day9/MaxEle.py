def findmax(l,start,end,m):
    if start==end:
        if m < l[start]:
            # print(m)
            m = l[start]
            return m
    if start>end:
        return m
    if start<end:
        mid = start+(end-start)//2
        ans = findmax(l,start,mid,m)
        ans = findmax(l,mid+1,end,m)
        return ans
l = list(map(int,input().split()))
m = l[0]
print(findmax(l,0,len(l)-1,m))
print(m)