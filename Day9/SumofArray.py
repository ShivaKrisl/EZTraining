def findsum(l,start,end,ans):
    if start==end:
        # print(l[start])
        ans+=l[start]
        return ans
    
    if start>end:
        return ans
    
    if start<end:
        mid = start+(end-start)//2
        ans = findsum(l,start,mid,ans)
        ans = findsum(l,mid+1,end,ans)
        return ans
l = list(map(int,input().split()))
ans = 0
print(findsum(l,0,len(l)-1,ans))
