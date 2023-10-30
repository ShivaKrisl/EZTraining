# https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def gcd(self,a,b):
        if b==0:
            return a
        return gcd(b%a,a)

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next==None:
            return head
        slow = head
        fast = head.next
        while fast!=None:
            val = self.gcd(slow.val,fast.val)
            t = ListNode(val)
            t1 = slow.next
            slow.next = t
            t.next = t1
            slow = fast
            fast = fast.next
        return head