# https://leetcode.com/problems/range-sum-of-bst/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def preorder(self,root,ans,low,high):
        if root==None:
            return ans
        if root.val>=low and root.val<=high:
            ans+=root.val
        ans = self.preorder(root.left,ans,low,high)
        ans = self.preorder(root.right,ans,low,high)
        return ans
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return self.preorder(root,0,low,high)