import time as t
def search(l,index,ans,ele):
    if index==len(l):
        return ans
    if l[index] == ele:
        ans.append(index)
    return search(l,index+1,ans,ele)

def searcher(l,index,ele):
    t = []
    if index==len(l):
        return t
    if l[index]==ele:
        t.append(index)
    p = (searcher(l,index+1,ele))
    if len(t)!=0:
        p.append(t)
    return p
l = [1,2,4,3,4,5]
s = t.time()
print(searcher(l,0,5))
e = t.time()
print(e-s)