a,b = map(int,input("Enter 2 numbers = ").split())
res = a*b
while b!=0:
    a,b = b,a%b
print("LCM = ",(res)//a)