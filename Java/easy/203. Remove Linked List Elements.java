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
    public ListNode removeElements(ListNode head, int val) {
        ListNode dummy = new ListNode(0, head);
        ListNode curNode = dummy;
        while (curNode != null) {
            while (curNode.next != null && curNode.next.val == val) curNode.next = curNode.next.next;
            curNode = curNode.next;
        }
        return dummy.next;
    }
}