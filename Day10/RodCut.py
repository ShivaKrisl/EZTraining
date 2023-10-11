def cutter(n,a,b,c,dc):
    if n==0:
        return dc
    if n<a or n<b or n<c:
        return -1
    first = cutter(n-a,a,b,c,dc+1)
    second = cutter(n-b,a,b,c,dc+1)
    third = cutter(n-c,a,b,c,dc+1)
    m = max(first,second,third)
    return m if m>0 else -1
n = int(input())
a,b,c = map(int,input().split())
print(cutter(n,a,b,c,0))