n = int(input())
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
for i in range(1,n+1):
    j = i-1
    k = 0
    while(j>=0):
        k += 10**(j)*i
        j-=1
    print(k)