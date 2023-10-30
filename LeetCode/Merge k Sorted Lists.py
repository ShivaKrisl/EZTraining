# https://leetcode.com/problems/merge-k-sorted-lists/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = []
        for lls in lists:
            temp = lls
            while temp!=None:
                res.append(temp.val)
                temp = temp.next
        new = ListNode()
        temp = new
        res.sort()
        for i in res:
            temp.next = ListNode(i)
            temp = temp.next
        return new.next