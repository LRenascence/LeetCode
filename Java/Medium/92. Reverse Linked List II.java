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
    public ListNode reverseBetween(ListNode head, int m, int n) {
        if (head == null) return head;
        ListNode dummy = new ListNode(0, head);
        ListNode prevNode = dummy;
        int index = 0;
        while (index++ < m - 1) prevNode = prevNode.next;
        ListNode start = prevNode;
        ListNode end = start.next;
        ListNode curNode = end.next;
        while (m++ < n) {
            end.next = curNode.next;
            curNode.next = start.next;
            start.next = curNode;
            curNode = end.next;
        }
        return dummy.next;
    }
}