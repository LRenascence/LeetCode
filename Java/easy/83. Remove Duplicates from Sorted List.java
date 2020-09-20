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
        ListNode curNode = head;
        while (curNode != null) {
            while (curNode.next != null && curNode.next.val == curNode.val) curNode.next = curNode.next.next;
            curNode = curNode.next;
        }
        return head;
    }
}