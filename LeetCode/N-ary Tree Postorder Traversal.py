# https://leetcode.com/problems/n-ary-tree-postorder-traversal/
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postOrder(self,root,l):
        if root==None:
            return l
        for i in root.children:
            l = self.postOrder(i,l)
        l.append(root.val)
        return l
    def postorder(self, root: 'Node') -> List[int]:
        l = []
        return self.postOrder(root,l)