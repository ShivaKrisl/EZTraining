# https://leetcode.com/problems/find-the-k-beauty-of-a-number/
class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        dc = 0
        if num<10:
            return 1
        x = str(num)
        res = ""
        res+=x[0]
        size = 1
        j = 1
        while j<len(x):
            if size<k:
                res+=x[j]
                j+=1
                size+=1
            if size==k:
                if int(res)!=0 and num%(int(res))==0:
                    dc+=1
                res = res[1:]
                size-=1
        return dc