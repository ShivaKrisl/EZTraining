import math
n = int(input("Enter a number = "))
fact = 1
if n==0 or n==1:
    print(fact)
else:
    while(n):
        fact*=n
        n-=1
print(fact)