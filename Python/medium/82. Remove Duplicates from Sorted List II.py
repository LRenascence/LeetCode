"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Return the linked list sorted as well.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0, head)
        dummyIter = dummy
        curNode = dummy.next
        while curNode != None:
            dup = False
            while curNode.next and curNode.val == curNode.next.val:
                curNode = curNode.next
                dup = True
            if dup:
                curNode = curNode.next
                continue
            dummyIter.next = curNode
            dummyIter = dummyIter.next
            curNode = curNode.next
        dummyIter.next = curNode
        return dummy.next