# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        curNode = dummy
        while l1 and l2:
            if l1.val < l2.val:
                curNode.next = l1
                l1 = l1.next
            else:
                curNode.next = l2
                l2 = l2.next
            curNode = curNode.next
        if l1:
            curNode.next = l1
        elif l2:
            curNode.next = l2
        return dummy.next