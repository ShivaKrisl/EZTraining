# https://leetcode.com/problems/odd-even-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        even = ListNode()
        p1 = even
        odd = ListNode()
        p2 = odd
        index=1
        temp = head
        while temp!=None:
            if index%2==0:
                p1.next = ListNode(temp.val)
                p1 = p1.next
                temp = temp.next
            else:
                p2.next= ListNode(temp.val)
                p2 = p2.next
                temp = temp.next
            index+=1
            # dc+=1
        # print(dc)
        odd = odd.next
        even = even.next
        p2.next = even
        return odd