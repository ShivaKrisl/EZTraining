l = list(map(int,input().split()))
target = int(input())
start = 0
end = len(l)-1
while(start<end):
    if l[start]+l[end]==target:
        print([start,end])
        break
    elif l[start]+l[end]>target:
        end-=1
    if l[start]+l[end]<target:
        start+=1
if(start>=end):
    print([-1,-1])