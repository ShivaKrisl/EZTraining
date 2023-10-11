w = list(map(int,input().split()))
pr = list(map(int,input().split()))
ca = int(input())
perkg = []
for i in range(len(w)):
    perkg.append(pr[i]/w[i])
l = list(zip(w,pr,perkg))

l.sort(key = lambda x:x[2],reverse=True)
print(l)
profit = 0
for wts,prs,pkr in l:
    if wts<=ca:
        profit+=prs
        ca-=wts
    else:
        profit+=ca*(pkr)
        break
print(profit)