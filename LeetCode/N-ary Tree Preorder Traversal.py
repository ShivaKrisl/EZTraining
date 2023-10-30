# https://leetcode.com/problems/n-ary-tree-preorder-traversal/
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preOrder(self,root,l):
        if root == None:
            return l
        l.append(root.val)
        for i in root.children:
            l = self.preOrder(i,l)
        return l
    def preorder(self, root: 'Node') -> List[int]:
        l = []
        return self.preOrder(root,l)