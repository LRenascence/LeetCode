"""
Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

 

Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        curNode = head
        length = 0
        while curNode != None:
            curNode = curNode.next
            length += 1
        def mergeSort(head, length):
            if head and not head.next:  return head
            leftList = ListNode()
            rightList = ListNode()
            leftIter = leftList
            rightIter = rightList
            counter = 0
            curNode = head
            while curNode != None:
                if counter < length // 2:
                    leftIter.next = curNode
                    leftIter = leftIter.next
                else:
                    rightIter.next = curNode
                    rightIter = rightIter.next
                curNode = curNode.next
                counter += 1
            leftIter.next = None
            rightIter.next = None
            leftList = mergeSort(leftList.next, length // 2)
            if length % 2 == 0:
                rightList = mergeSort(rightList.next, length // 2)
            else:
                rightList = mergeSort(rightList.next, (length // 2) + 1)
            dummy = ListNode()
            dummyIter = dummy
            while leftList and rightList:
                if leftList.val < rightList.val:
                    dummyIter.next = leftList
                    leftList = leftList.next
                else:
                    dummyIter.next = rightList
                    rightList = rightList.next
                dummyIter = dummyIter.next
            if leftList:
                dummyIter.next = leftList
            elif rightList:
                dummyIter.next = rightList
            return dummy.next
        return mergeSort(head, length)