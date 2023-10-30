# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def insertBegin(self,val,rev):
        node = ListNode(val)
        node.next = rev
        rev = node
        return rev

    def pairSum(self, head: Optional[ListNode]) -> int:
        if head.next.next==None:
            return head.val+head.next.val
        rev = ListNode()
        temp = head
        while temp!=None:
            rev = self.insertBegin(temp.val,rev)
            temp = temp.next

        temp = rev
        t2 = head
        maxi = -1
        while t2!=None:
            maxi = max(maxi,temp.val+t2.val)
            temp = temp.next
            t2 = t2.next
        return maxi