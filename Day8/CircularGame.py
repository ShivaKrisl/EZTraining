class Solution:
    def finder(self,l,start,k):
        if len(l)==1:
            return l[0]
        if k>len(l)-1:
            k = k-len(l)
        if start>len(l)-1:
            start = start-len(l)
            k = k-start
        if start==k:
            del(l[start])
            start = start-1
            k = k+1
        print(l)
        return self.finder(l,start+1,k)
    def findTheWinner(self, n,k):
        l = [i for i in range(1,n+1)]
        return self.finder(l,0,k-1)
obj = Solution()
print(obj.findTheWinner(6,5))