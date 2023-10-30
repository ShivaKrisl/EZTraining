# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        res = []
        temp = head
        while temp!=None:
            res.append(temp.val)
            temp = temp.next
        if k>len(res):
            k = k%len(res)
        res[k-1],res[len(res)-k] = res[len(res)-k],res[k-1]
        print(res)
        new = ListNode()
        temp = new
        for i in res:
            temp.next = ListNode(i)
            temp = temp.next
        return new.next
