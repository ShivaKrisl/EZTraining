def printer(n):
    if n==0:
        return
    printer(n-1)
    print(n,end = " ")

def printrev(n):
    if n==0:
        return
    print(n,end = " ")
    printrev(n-1)
n = int(input("Enter stop = "))
printer(n)
print()
printrev(n)