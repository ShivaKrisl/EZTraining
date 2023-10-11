def BS(l,start,end,se):
    if start>end:
        print("Element Not Found")
        return
    mid = start+(end-start)//2
    if l[mid]==se:
        return f"Element Found at index = {mid}"
    if l[mid]>se:
        return BS(l,start,mid-1,se)
    return BS(l,mid+1,end,se)
l = list(map(int,input().split()))
se = int(input("Enter search element = "))
print(BS(l,0,len(l)-1,se))