"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.
"""

# slow
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = ListNode()
        dummyIter = dummy
        lists = [lst for lst in lists if lst]
        while lists:
            curList = lists[0]
            curVal = curList.val
            index = 0
            for i in range(len(lists)):
                if lists[i].val < curVal:
                    curVal = lists[i].val
                    index = i
            dummyIter.next = lists[index]
            dummyIter = dummyIter.next
            lists[index] = lists[index].next
            if not lists[index]:
                lists.pop(index)
        dummyIter.next = None
        return dummy.next


# fast
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = ListNode()
        dummyIter = dummy
        heap = []
        for lst in lists:
            while lst:
                heapq.heappush(heap, lst.val)
                lst = lst.next
        while heap:
            dummyIter.next = ListNode(heapq.heappop(heap))
            dummyIter = dummyIter.next
        dummyIter.next = None
        return dummy.next