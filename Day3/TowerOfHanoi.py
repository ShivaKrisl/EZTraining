import math
def tower(n,ans):
    if n==1:
        return 2*ans-1
    return tower(n-1,2*ans)

n = int(input("Enter no.of disks = "))
ans=1
print(tower(n,ans))
# print(int(math.pow(2,n))-1)