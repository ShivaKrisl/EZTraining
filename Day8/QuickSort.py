# def divider(l):
#     # if start<end:
#     #     mid = start+(end-start)//2
#     #     print(l[start:mid])
#     #     print(l[mid+1:end+1])
#     #     divider(l,start,mid)
#     #     divider(l,mid+1,end)
#     if len(l)>=1:
#         mid = len(l)//2
#         print(l)
#         divider(l[:mid])
#         divider(l[mid+1:])
# l = [3,5,1,2,0,9,8]
# divider(l)


def quicksort(l,start,end):
    if start<end:
        i = start
        j = end
        pivot = start
        while i<j:
            while i<end and l[i]<=l[pivot]:
                i+=1
            while j>0 and l[j]>l[pivot]:
                j-=1
            if i<j:
                l[i],l[j] = l[j],l[i]
            l[pivot],l[j] = l[j],l[pivot]
            quicksort(l,start,pivot-1)
            quicksort(l,pivot+1,end)
print(quicksort([3,2,4,5,1],0,4))
