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
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode result = new ListNode(0);
        ListNode resultIter = result;
        while (l1 != null && l2 != null) {
            if (l1.val < l2.val) {
                resultIter.next = l1;
                l1 = l1.next;
            }
            else {
                resultIter.next = l2;
                l2 = l2.next;
            }
            resultIter = resultIter.next;
        }
        if (l1 == null) resultIter.next = l2;
        else if (l2 == null) resultIter.next = l1;
        return result.next;
    }
}