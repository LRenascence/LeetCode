"""
Reverse a singly linked list.
Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:
A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# iterative solution
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        curNode1 = head.next
        curNode2 = head
        head.next = None
        while curNode1 != None:
            temp = curNode1.next
            curNode1.next = curNode2
            curNode2 = curNode1
            curNode1 = temp
        return curNode2

# recursive solution
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        newHead =  self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newHead

