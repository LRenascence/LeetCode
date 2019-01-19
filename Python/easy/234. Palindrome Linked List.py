"""
Given a singly linked list, determine if it is a palindrome.
Example 1:
Input: 1->2
Output: false
Example 2:
Input: 1->2->2->1
Output: true
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# easiest solution, O(n) space
class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        curNode = head
        valList = []
        while curNode != None:
            valList.append(curNode.val)
            curNode = curNode.next
        for i in range(int(len(valList) / 2)):
            if valList[i] != valList[-i - 1]:
                return False
        return True

# change the linked list, O(1) space
class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        preVal = None
        while slow != None:
            temp = slow.next
            slow.next = preVal
            preVal = slow
            slow = temp
        curNode = head
        while  preVal != None:
            if preVal.val != curNode.val:
                return False
            curNode = curNode.next
            preVal = preVal.next
        return True

# change the linked list but restore it at the end, O(1) space
class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        preVal = None
        while slow != None:
            temp = slow.next
            slow.next = preVal
            preVal = slow
            slow = temp
        curNode = head
        nextVal = None
        while preVal != None:
            if preVal.val != curNode.val:
                return False
            curNode = curNode.next
            temp = preVal.next
            preVal.next = nextVal
            nextVal = preVal
            preVal = temp
        return True
