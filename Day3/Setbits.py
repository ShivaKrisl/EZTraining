n = int(input("Enter a number = "))
if n<0:
    n = -(n+1)
# LOGIC -1
# s = bin(n)
# dc=0
# for i in s:
#     if i=='1':
#         dc+=1
# print(dc)

# LOGIC 2
# dc = 0
# while(n):
#     dc+=1
#     n = n&(n-1)
# print(dc)

# LOGIC 3
dc = 0
while(n):
    if(n&1):
        dc+=1
    n = n>>1
print(dc)