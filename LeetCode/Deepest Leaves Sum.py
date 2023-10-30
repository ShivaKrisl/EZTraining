# https://leetcode.com/problems/deepest-leaves-sum/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def inorder(self,root,depth,maxdepth,ans):
        if root.left==None and root.right==None:
            if depth==maxdepth-1:
                ans+=root.val
            return ans
        if root.left:
            ans = self.inorder(root.left,depth+1,maxdepth,ans)
        if root.right:
            ans = self.inorder(root.right,depth+1,maxdepth,ans)
        return ans

    def findDepth(self,root,depth):
        if root==None:
            return depth
        left = self.findDepth(root.left,depth+1)
        right = self.findDepth(root.right,depth+1)
        if left>right:
            return left
        return right
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        maxdepth = self.findDepth(root,0)
        print(maxdepth)
        if root.left==None and root.right==None:
            return root.val
        else:
            return self.inorder(root,0,maxdepth,0)