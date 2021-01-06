# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        prevNode = dummy
        nextNode = dummy.next
        while nextNode:
            curVal = nextNode.val
            duplicate = False
            while nextNode.next and curVal == nextNode.next.val:
                nextNode = nextNode.next
                duplicate = True
            if duplicate:
                nextNode = nextNode.next
            else:
                prevNode.next = nextNode
                prevNode = prevNode.next
                if nextNode:
                    nextNode = nextNode.next
        prevNode.next = None
        return dummy.next