# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        elif len(s)==1:
            return 1
        ans = ""
        maxi  = -1
        j = 1
        ans+=s[0]
        while j<len(s):
            if s[j] not in ans:
                ans+=s[j]
                j+=1
            else:
                if maxi<len(ans):
                    maxi = len(ans)
                # print(res)
                ans  = ans[1:]
                # j+=1
                # ans= ans[i:]
            if maxi < len(ans):
                    maxi = len(ans)
        # print(res)
        return maxi