"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return None
        length = 0
        curNode = head
        while curNode:
            length += 1
            curNode = curNode.next
        if n == length:
            return head.next
        index = 1
        curNode = head
        while index < length - n:
            curNode = curNode.next
            index += 1
        if curNode.next:
            curNode.next = curNode.next.next
        else:
            curNode.next = None
        return head

# use list to store listnode
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return None
        listNodeList = []
        curNode = head
        while curNode:
            listNodeList.append(curNode)
            curNode = curNode.next
        N = len(listNodeList)
        if n == N:
            return head.next
        listNodeList[N - n - 1].next = listNodeList[N - n - 1].next.next
        return head

# two pointers one pass
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return None
        slow = fast = head
        dist = 0
        while dist < n:
            fast = fast.next
            dist += 1
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head