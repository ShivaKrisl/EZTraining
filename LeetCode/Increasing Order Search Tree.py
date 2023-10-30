# https://leetcode.com/problems/increasing-order-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,root,l):
        if root == None:
            # l.append(None)
            return l
        l = self.inorder(root.left,l)
        l.append(root.val)
        l = self.inorder(root.right,l)
        return l
        
    def increasingBST(self, root: TreeNode) -> TreeNode:
        l = []
        l = self.inorder(root,l)
        print(l)
        new = TreeNode()
        temp = new
        for i in l:
            temp.right = TreeNode(i)
            temp = temp.right
        return new.right