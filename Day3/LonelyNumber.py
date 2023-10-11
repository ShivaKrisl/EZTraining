l = list(map(int,input().split()))
# print(len(l))
res=0
if len(l)%2!=0:
    res=l[0]
for i in range(len(l)):
    res^=l[i]
print(res)