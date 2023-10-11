l = list(map(int,input().split()))
print(sum([i for i in range(min(l),max(l)+1)]) - sum(l))

