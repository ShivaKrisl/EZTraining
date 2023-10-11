l = list(map(int,input().split()))
count = [0 for i in range(len(l)+1)]
# print(len(count))
for i in range(len(l)):
    count[l[i]]+=1
for i in range(1,len(count)):
    count[i] += count[i-1]
res = [0 for i in range(len(l))]
for i in range(len(l)-1,-1,-1):
    res[count[l[i]]-1] = l[i]
    count[l[i]]-=1
print(res)