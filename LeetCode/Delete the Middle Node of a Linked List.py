# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next==None:
            head = None
            return head
        slow = head
        fast = head
        t = None
        while fast!=None and fast.next!=None:
            t = slow
            slow = slow.next
            fast = fast.next.next
        t.next = t.next.next
        return head