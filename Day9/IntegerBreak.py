def findsetter(n):
    pass

def IntegerBreak(n):
    outer = []
    for i in range(1,n):
        internal = []
        j = i
        j = findsetter(j)
        s=0
        while j>0:
            if s+j>n:
                j=j-1
            else:
                s+=j
                internal.append(j)
        outer.append(internal)
    return outer
n = 10
print(*(IntegerBreak(n)))