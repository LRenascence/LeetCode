"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# My slow solution
class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode()
        if l1 != None and l2 != None:
            if l1.val <= l2.val:
                l3.val = l1.val
                l1 = l1.next
            else:
                l3.val = l2.val
                l2 = l2.next
        else:
            if l1 == None and l2 != None:
                l3.val = l2.val
                l2 = l2.next
            elif l2 == None and l1 != None:
                l3.val = l1.val
                l1 = l1.next
            else:
                return None
        l3Cur = l3
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                l3Next = ListNode(l1.val)
                l3Cur.next = l3Next
                l3Cur = l3Cur.next
                l1 = l1.next
            else:
                l3Next = ListNode(l2.val)
                l3Cur.next = l3Next
                l3Cur = l3Cur.next
                l2 = l2.next
        if l1 == None:
            while l2 != None:
                l3Next = ListNode(l2.val)
                l3Cur.next = l3Next
                l3Cur = l3Cur.next
                l2 = l2.next
        else:
            while l1 != None:
                l3Next = ListNode(l1.val)
                l3Cur.next = l3Next
                l3Cur = l3Cur.next
                l1 = l1.next
        return l3

# Good solution
class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = cur = ListNode()
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1 == None:
            cur.next = l2
        else:
            cur.next = l1
        return l3.next