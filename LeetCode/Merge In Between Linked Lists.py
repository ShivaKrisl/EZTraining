# https://leetcode.com/problems/merge-in-between-linked-lists/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # temp = list1
        # prev = None
        # while temp.val!=a:
        #     prev = temp
        #     temp = temp.next

        # prev.next = list2
        # while temp.val!=b:
        #     # print(temp.val)
        #     temp = temp.next
        # temp = temp.next
        # se = list2
        # while se.next!=None:
        #     se=se.next
        # se.next = temp
        # return list1

        temp = list1
        index = 0
        while index!=a-1:
            index+=1
            # print(temp.val)
            temp = temp.next
        pr = temp

        while index!=b:
            index+=1
            print(temp.val)
            temp = temp.next
        temp = temp.next
        pr.next = list2
        se = list2
        while se.next!=None:
            se = se.next
        se.next = temp
        return list1