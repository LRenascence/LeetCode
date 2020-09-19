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
    public ListNode reverseList(ListNode head) {
        if (head == null || head.next == null) return head;
        ListNode prevNode = head;
        ListNode nextNode = head.next;
        head.next = null;
        while (nextNode != null) {
            ListNode tempNode = new ListNode();
            tempNode = nextNode.next;
            nextNode.next = prevNode;
            prevNode = nextNode;
            nextNode = tempNode;
        }
        return prevNode;
    }
}