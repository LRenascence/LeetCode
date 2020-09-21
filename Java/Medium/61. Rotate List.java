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
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null) return head;
        int listLen = 1;
        ListNode curNode = head;
        while (curNode.next != null) {
            curNode = curNode.next;
            listLen++;
        }
        curNode.next = head;
        k %= listLen;
        ListNode newHead = head;
        int index = 1;
        while (index++ < listLen - k) {
            newHead = newHead.next;
        }
        ListNode temp = newHead.next;
        newHead.next = null;
        newHead = temp;
        return newHead;
    }
}