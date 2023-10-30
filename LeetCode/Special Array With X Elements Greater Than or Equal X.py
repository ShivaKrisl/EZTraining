# https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        x = 0
        while True:
            s = len([i for i in nums if i>=x])
            if s==x:
                return x
            elif x>s:
                return -1
            x = x+1
        return -1