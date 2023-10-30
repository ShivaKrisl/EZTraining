# https://leetcode.com/problems/symmetric-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def preorder(self,root,left):
        if root == None:
            left.append(None)
            return left
        left.append(root.val)
        left = self.preorder(root.left,left)
        left = self.preorder(root.right,left)
        return left
    def postorder(self,root,right):
        if root == None:
            right.append(None)
            return right
        right = self.postorder(root.left,right)
        right = self.postorder(root.right,right)
        right.append(root.val)
        return right
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root==None:
            return True
        if root.left==None and root.right!=None:
            return False
        if root.left!=None and root.right == None:
            return False
        if root.left==None and root.right==None:
            return True
        left = []
        right = []
        left = self.preorder(root.left,left)
        right = self.postorder(root.right,right)
        print(left)
        print(right)
        if left!=right[::-1]:
            return False
        return True