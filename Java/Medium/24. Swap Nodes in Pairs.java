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
    public ListNode swapPairs(ListNode head) {
        if (head == null || head.next == null) return head;
        ListNode dummy = new ListNode(0, null);
        ListNode prevNode = dummy;
        ListNode middleNode = head;
        ListNode nextNode = head.next;
        while (middleNode != null && nextNode != null) {
            middleNode.next = nextNode.next;
            nextNode.next = middleNode;
            prevNode.next = nextNode;
            
            if (middleNode.next == null) break;
            prevNode = middleNode;
            middleNode = middleNode.next;
            nextNode = middleNode.next;
        }
        return dummy.next;
    }
}