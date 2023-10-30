# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        res = []
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                ans = ""
                for k in range(i,j+1):
                    ans+=s[k]
                if len(set(ans))==len(ans) and len(ans)==3:
                    res.append(ans)
        print(res)
        return len(res)