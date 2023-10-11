n = int(input("Enter number = "))
p = int(input("Enter pos = "))
# LOGIC-1  
# if n&(1<<(i-1)):
#     print("Yes")
# else:
#     print("No")

# LOGIC -3
s = bin(n)
for i in range(len(s)-1,2,-1):
    if i==p:
        if s[i]=='1':
            print("YES")
        else:
            print("NO")
        break