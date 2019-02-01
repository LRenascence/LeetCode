"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode(0)
        curNode1 = l1
        curNode2 = l2
        curNode3 = l3
        carry = 0
        while curNode1 and curNode2:
            sum = curNode1.val + curNode2.val + carry
            if sum > 9:
                sum -= 10
                carry = 1
            else:
                carry = 0
            curNode3.next = ListNode(sum)
            curNode1 = curNode1.next
            curNode2 = curNode2.next
            curNode3 = curNode3.next
        if curNode1:
            [curNode3, carry] = self.add(curNode1, curNode3, carry)
        else:
            [curNode3, carry] = self.add(curNode2, curNode3, carry)
        if carry != 0:
            curNode3.next = ListNode(1)
        return l3.next

    def add(self, l1, l2, carry):
        while l1:
            sum = l1.val + carry
            if sum > 9:
                sum -= 10
                carry = 1
            else:
                carry = 0
            l2.next = ListNode(sum)
            l1 = l1.next
            l2 = l2.next
        return [l2, carry]

# short version
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyHead = ListNode(0)
        curNode1 = l1
        curNode2 = l2
        curNode3 = dummyHead
        carry = 0
        while curNode1 or curNode2:
            val1 = curNode1.val if curNode1 else 0
            val2 = curNode2.val if curNode2 else 0
            sum = val1 + val2 + carry
            if sum > 9:
                sum -= 10
                carry = 1
            else:
                carry = 0
            curNode3.next = ListNode(sum)
            curNode1 = curNode1.next if curNode1 else None
            curNode2 = curNode2.next if curNode2 else None
            curNode3 = curNode3.next
        if carry != 0:
            curNode3.next = ListNode(carry)
        return dummyHead.next