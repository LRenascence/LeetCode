/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        ListNode dummy = new ListNode(0, head);
        ListNode dummyIter = dummy;
        ListNode curNode = dummy.next;
        while (curNode != null) {
            boolean dup = false;
            while (curNode.next != null && curNode.next.val == curNode.val) {
                curNode= curNode.next;
                dup = true;
            }
            if (dup) {
                curNode = curNode.next;
                continue;
            }
            dummyIter.next = curNode;
            dummyIter = dummyIter.next;
            curNode = curNode.next;
        }
        dummyIter.next = curNode;
        return dummy.next;
    }
}