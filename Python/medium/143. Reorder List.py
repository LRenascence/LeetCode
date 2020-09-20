"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return head
        fastNode = slowNode = head
        while fastNode.next != None and fastNode.next.next != None:
            fastNode = fastNode.next.next
            slowNode = slowNode.next
        prevNode = None
        curNode = slowNode.next
        slowNode.next = None
        while curNode != None:
            temp = curNode.next
            curNode.next = prevNode
            prevNode = curNode
            curNode = temp
        curNode = head
        dummy = ListNode(0, head)
        dummyIter = dummy
        while prevNode != None:
            dummyIter.next = curNode
            dummyIter = dummyIter.next
            curNode = curNode.next
            dummyIter.next = prevNode
            dummyIter = dummyIter.next
            prevNode = prevNode.next
        if curNode:
            dummyIter.next = curNode
            dummyIter = dummyIter.next
        dummyIter.next = None
        return dummy.next
        