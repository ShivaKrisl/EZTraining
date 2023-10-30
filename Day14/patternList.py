l = list(map(int,input().split()))
# for i in range(len(l)):
#     print(i,'x '*l[i],sep=' ')
#     # print()
for i in range(max(l),-1,-1):
    for j in range(len(l)):
        if l[j]>=i:
            print('x',end='')
        else:
            print(' ',end='')
    print()
