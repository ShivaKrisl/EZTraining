# https://leetcode.com/problems/rotate-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next==None:
            return head
        if k==0:
            return head
        res = []
        temp = head
        while temp!=None:
            res.append(temp.val)
            temp = temp.next
        n = len(res)
        k = k%n
        # print(res)
        ans = []
        ind = 1
        while ind<=k:
            ans.append(res[n-ind])
            ind+=1
        ans = ans[::-1]
        # print(ans)
        res = ans+res[:n-k]
        # print(res)
        new = ListNode()
        temp = new
        for i in res:
            temp.next = ListNode(i)
            temp = temp.next
        return new.next