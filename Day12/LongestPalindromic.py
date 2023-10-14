def subseq(s,ans,res):
      if len(s)==0:
            # print(ans)
            res.append(ans)
            return res
      subseq(s[1:],ans+s[0],res)
      subseq(s[1:],ans,res)
      return res
s = input()
res = []
ans = ""
subseq(s,"",res)
for i in res:
     if i==i[::-1]:
          if len(i)>len(ans):
               ans = i
print(ans)