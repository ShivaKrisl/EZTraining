def summer(n,dc):
    if n==0:
        return dc
    return summer(n-1,dc+n)
n = int(input("Enter Stop = "))
print(summer(n,0))