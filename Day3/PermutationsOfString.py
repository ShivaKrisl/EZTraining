def permuatator(s,res):
    if len(s)==0:
        print(res)
        return
    for i in range(len(res)+1):
        first = res[0:i]
        second = s[0]
        third = res[i:len(res)]
        permuatator(s[1:],first+second+third)
s = input("Enter a string = ")
res=""
permuatator(s,res)