# https://leetcode.com/problems/minimum-string-length-after-removing-substrings/
class Solution:
    def minLength(self, s: str) -> int:
        l = []
        for i in range(len(s)):
            if s[i]=='B':
                if len(l)>0 and l[-1]=='A':
                    l.pop()
                else:
                    l.append('B')
            elif s[i]=='D':
                if len(l)>0 and l[-1]=='C':
                    l.pop()
                else:
                    l.append('D')
            else:
                l.append(s[i])
        return len(l)
    