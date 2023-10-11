import itertools
s = itertools.combinations('0',2)
for i in s:
    print(i)
# d = {'2':'abc',"3":'def','4':'ghi','5':'jkl'}
# s = '2345'
# # p = []
# l = []
# if len(s)==3:
#     for i in range(len(s)-1):
#         res = ""
#         res+=d[s[i]]
#         for v in d[s[i+1]]:
#             for k in d[s[len(s)-1]]:
#                     res+=v+k
#                     l.append(res)
#                     res=""
# elif len(s)==4:
#      for i in range(len(s)-3):
#           res = ""
#           res+=d[s[i]]
#           for v in d[s[i+1]]:
#                for k in d[s[i+2]]:
#                     res+=v+k
#                l.append(res)
#                res = ""
# else:
#     for i in range(len(s)-1):
#         l = []
#         # res = ""
#         for v in d[s[i]]:
#             res=""
#             for k in d[s[i+1]]:
#                 res+=v+k
#                 l.append(res)
#                 res = ""

# print(l)