import math
n = int(input("Enter a number = "))
if(int(math.log(n,2)) != math.log(n,2)):
    print("NOT POWER OF 2")
else:
    print("YES POWER OF 2")

if(int(math.log(n,4))!=math.log(n,4)):
    print("NOT POWER OF 4")
else:
    print("YES POWER OF 4")