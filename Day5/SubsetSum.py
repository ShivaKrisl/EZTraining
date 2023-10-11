def check(l,s):
    if s==0:
        return True
    if len(l)==0:
        return False
    return check(l[1:],s-l[0]) or check(l[1:],s)

l = [2,3,7,9,10]
l.sort()
s = 5
if s<l[0]:
    print(False)
else:
    print(check(l,s))