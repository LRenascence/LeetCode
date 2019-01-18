"""
Remove all elements from a linked list of integers that have value val.
Example:
Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head == None:
            return None
        while head.val == val:
            head = head.next
            if head == None:
                return None
        curNode1 = head.next
        curNode2 = head
        while curNode1 != None:
            if curNode1.val == val:
                curNode2.next = curNode1.next
                curNode1 = curNode1.next
            else:
                curNode1 = curNode1.next
                curNode2 = curNode2.next
        return head