# https://leetcode.com/problems/next-greater-element-i/
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in nums1:
            p = nums2.index(i)
            p = p+1
            # flag = 0
            while p<len(nums2):
                if nums2[p]>i:
                    res.append(nums2[p])
                    # flag==1
                    break
                p+=1
            if p==len(nums2):
                res.append(-1)
        return res