s = input()
i = 0
j = len(s)-1
while i!=j:
    if s[i]!=s[j]:
        print("not palindrome")
        break
    if i>j:
        break
    else:
        i+=1
        j-=1
if i>=j:
    print("palindrome")