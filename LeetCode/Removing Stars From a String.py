# https://leetcode.com/problems/removing-stars-from-a-string/
class Solution:
    def removeStars(self, s: str) -> str:
        l = []
        for i in range(len(s)):
            if s[i]=='*':
                if len(l)>0:
                    l.pop()
            else:
                l.append(s[i])
        if len(l)==0:
            return ""
        return "".join(l)