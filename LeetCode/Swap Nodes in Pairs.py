# https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        # l = []
        # temp = head
        # while temp!=None:
        #     l.append(temp.val)
        # for i in range(1,len(l),2):
        #     l[i-1],l[i] = l[i],l[i-1]
        # print(l)
        # new = ListNode()
        # temp = new
        # for i in l:
        #     temp.next = ListNode(i)
        #     temp = temp.next
        # return new.next

        dc=0
        temp = head
        while temp!=None:
            dc+=1
            temp = temp.next
        new = ListNode()
        temp = new
        fast = head.next
        slow = head
        if dc%2==0:
            while fast!=None:
                temp.next = ListNode(fast.val)
                temp = temp.next
                temp.next = ListNode(slow.val)
                temp = temp.next
                if fast.next==None:
                    break
                slow = fast.next
                fast = slow.next
            return new.next
        else:
            while fast!=None:
                temp.next = ListNode(fast.val)
                temp = temp.next
                temp.next = ListNode(slow.val)
                temp = temp.next
                if fast.next==None:
                    break
                slow = fast.next
                fast = slow.next
            temp.next = slow
            return new.next
        