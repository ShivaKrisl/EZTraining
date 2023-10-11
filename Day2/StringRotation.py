s=input()
s1=""
for c in s:
    if ((ord(c)>=65) and (ord(c)<=90)) or (ord(c)>=97 and ord(c)<=122) or (ord(c)>=48 and ord(c)<=57):
        s1+=c
s2=""
s2+=s1[::-1]
res=""
k=-1
for i in range(0,len(s)):
    if ((ord(s[i])>=65) and (ord(s[i])<=90)) or (ord(s[i])>=97 and ord(s[i])<=122) or (ord(c)>=48 and ord(c)<=57):
        k+=1 
        res+=s2[k]
    else:
        res+=s[i]
print(res)