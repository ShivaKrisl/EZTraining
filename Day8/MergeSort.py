def divider(l,start,end):
    if start<end:
        mid = start + (end-start)//2
        print(l[start:mid+1])
        print(l[mid+1:end+1])
        divider(l,start,mid)
        divider(l,mid+1,end)

l = [3,4,5,2,1]
divider(l,0,len(l)-1)
    