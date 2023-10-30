# https://leetcode.com/problems/merge-nodes-in-between-zeros/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head.next
        res = 0
        new = ListNode()
        temp = new
        while fast!=None:
            if fast.val!=0:
                res+=fast.val
            else:
                t = ListNode(res)
                temp.next = t
                temp = temp.next
                res = 0
                slow = fast
            fast = fast.next
        new = new.next
        return new