def palindrome(s,i,j):
    if i>j:
        return True
    if s[i]!=s[j]:
        return False
    return palindrome(s,i+1,j-1)

def method2(res,s,i):
    if i<0:
        return res
    return method2(res+s[i],s,i-1)

s = input("Enter a string = ")
if palindrome(s,0,len(s)-1)==False:
    print("Not")
else:
    print("Yes")

if method2("",s,len(s)-1)==s:
    print("Palindrome")
else:
    print("Not Palindrome")