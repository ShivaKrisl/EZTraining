# https://leetcode.com/problems/rotate-array/
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        x = len(nums)
        l = nums[x-k:]+nums[:x-k]
        for i in range(x):
            nums[i] = l[i]