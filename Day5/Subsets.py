# def subsets(res,l):
#     t = []
#     if len(l)==0:
#         t.append(res)
#         return t
#     first = []
#     second = []
#     first = subsets(res.append(l[0]),l[1:])
#     second = subsets(res,l[1:])
#     first.append(second)
#     return first

def subsetsprint(res,l,ans):
    if len(l)==0:
        ans.append(res)
        return ans
    ans = subsetsprint(res+l[0:1],l[1:],ans)
    ans = subsetsprint(res,l[1:],ans)
    return ans

l = [1,2,3]
ans = []
res = []
# print(type(res))
print(subsetsprint(res,l,ans))
# print(subsets(res,l))

# def subseq(res,s,p):
#     t = []
#     if len(s)==0:
#         t.append(res)
#         return t
#     left = subseq(res+s[0],s[1:],p)
#     right = subseq(res,s[1:],p)
#     p.append(left)
#     p.append(right)
#     return p


# s = "abc"
# print(subseq("",s,[]))