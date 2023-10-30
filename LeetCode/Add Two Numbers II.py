# https://leetcode.com/problems/add-two-numbers-ii/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        t1 = l1
        t2 = l2
        r1 = ""
        r2 = ""
        while t1!=None:
            r1+=str(t1.val)
            t1 = t1.next
        while t2!=None:
            r2+=str(t2.val)
            t2 = t2.next
        ans = str(int(r1)+int(r2))
        l3 = ListNode()
        temp = l3
        for i in ans:
            temp.next=ListNode(int(i))
            temp = temp.next
        return l3.next