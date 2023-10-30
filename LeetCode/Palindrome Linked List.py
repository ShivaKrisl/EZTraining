# https://leetcode.com/problems/palindrome-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head ==None or head.next==None:
            return True
        l = []
        temp = head
        while temp!=None:
            l.append(temp.val)
            temp = temp.next
        if l==l[::-1]:
            return True
        return False