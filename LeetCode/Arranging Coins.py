# https://leetcode.com/problems/arranging-coins/
class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n==0 or n==1:
            return n
        else:
            # res = []
            # for i in range(1,n+1):
            #     l = []
            #     for j in range(1,i+1):
            #         l.append(1)
            #     res.append(l)
            # print(res)
            # s = 0
            # for i in range(len(res)):
            #     s+= sum(res[i])
            #     print(s)
            #     if s==n:
            #         return len(res[i])
            #     elif s>n:
            #         return len(res[i-1])
            s = 0
            for i in range(1,n+1):
                s+=i
                if s==n:
                    return i
                elif s>n:
                    return i-1
            