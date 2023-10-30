# https://leetcode.com/problems/sort-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        res = []
        temp = head
        while temp!=None:
            res.append(temp.val)
            temp = temp.next
        res.sort()
        new = ListNode()
        temp = new
        for i in res:
            temp.next = ListNode(i)
            temp = temp.next
        return new.next