"""
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# simulate rotation in an opposite direction
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        # find the tial first
        curHead = head
        curNode = head
        listLen = 1
        while curNode.next:
            listLen += 1
            curNode = curNode.next
        curTail = curNode
        # simulate the rotation in an opposite direction
        k %= listLen
        if k != 0:
            k = listLen - k
        while k > 0:
            changedNode = curHead
            curHead = curHead.next
            changedNode.next = None
            curTail.next = changedNode
            curTail = changedNode
            k -= 1
        return curHead

