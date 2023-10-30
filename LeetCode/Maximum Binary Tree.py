# https://leetcode.com/problems/maximum-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def divider(nums):
            if not nums: return None
            maxi,p=float('-inf'),-1
            for i in range(len(nums)):
                if nums[i]>maxi:
                    maxi=nums[i]
                    p=i
            root=TreeNode(maxi)
            root.left,root.right=divider(nums[0:p]),divider(nums[p+1:])
            return root
        return divider(nums)
