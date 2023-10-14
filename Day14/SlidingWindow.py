# def sumtar(l,tar,i,j):
#     if l[i]==tar:
#         return [l[0]]
#     j = i+1
#     while i<len(l) and j<len(l):
#         if sum(l[i:j+1])==tar:
#             return l[i:j+1]
#         elif j<len(l) and sum(l[i:j+1])<tar:
#             j+=1
#         elif sum(l[i:j+1])>tar:
#             i+=1

def sumtar(l,tar,i,j):
    if l[i]==tar:
        return [l[0]]
    j = 0
    cs = l[i]
    while j<len(l)-1:
        if cs==tar:
            return l[i:j+1]
        elif j<len(l) and cs<tar:
            # cs+=l[j]
            j+=1
            cs+=l[j]
        elif cs>tar:
            cs-=l[i]
            i+=1
    return None

l = list(map(int,input().split()))
tar = int(input())
print(sumtar(l,tar,0,0))
