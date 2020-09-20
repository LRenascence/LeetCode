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
    public ListNode oddEvenList(ListNode head) {
        if (head == null || head.next == null) return head;
        ListNode oddHead = head;
        ListNode evenHead = head.next;
        ListNode oddIter = oddHead;
        ListNode evenIter = evenHead;
        ListNode curNode = evenIter.next;
        int counter = 1;
        while (curNode != null) {
            if (counter == 0) {
                evenIter.next = curNode;
                evenIter = evenIter.next;
            }
            else {
                oddIter.next = curNode;
                oddIter = oddIter.next;
            }
            counter ^= 1;
            curNode = curNode.next;
        }
        oddIter.next = evenHead;
        evenIter.next = null;
        return oddHead;
    }
}