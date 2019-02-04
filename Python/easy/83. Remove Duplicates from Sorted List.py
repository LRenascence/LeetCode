"""
Given a sorted linked list, delete all duplicates such that each element appear only once.
Example 1:
Input: 1->1->2
Output: 1->2
Example 2:
Input: 1->1->2->3->3
Output: 1->2->3
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplicates(self, head: 'ListNode') -> 'ListNode':
        if not head or not head.next:
            return head
        valSet = set()
        valSet.add(head.val)
        curNode = head.next
        prevNode = head
        while curNode != None:
            if curNode.val not in valSet:
                valSet.add(curNode.val)
                curNode = curNode.next
                prevNode = prevNode.next
            else:
                curNode = curNode.next
                prevNode.next = curNode
        return head