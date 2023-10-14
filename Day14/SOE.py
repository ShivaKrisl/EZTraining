def primes(s,r):
    l = [True for i in range(r+1)]
    l[0] = False
    l[1]=False
    l[2] = True
    for i in range(r+1):
        if l[i]==True:
            j=i+1
            while j<r+1:
                if l[j]==True and j%i==0:
                    l[j]=False
                j+=1       
    return l
ans = primes(3,100)
for i in range(3,len(ans)):
    if ans[i]:
        print(i,end=" ")