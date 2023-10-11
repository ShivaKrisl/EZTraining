def find(l,tar):
    # res = []
    for i in range(len(l)-3):
        start = i+1
        end = len(l)-1
        while(start<end):
            if(l[start]+l[end]+l[i]==tar):
                # res.append([i,start,end])
                print(l[i],l[start],l[end])
                return True
            elif(l[start]+l[end]+l[i]<tar):
                start+=1
            else:
                end-=1
    # return res
    return False
l = list(map(int ,input().split()))
tar = int(input())
l.sort()
print(find(l,tar))

            
