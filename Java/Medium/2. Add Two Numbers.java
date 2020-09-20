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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode l1Iter = l1;
        ListNode l2Iter = l2;
        ListNode result = new ListNode(0);
        ListNode resultIter = result;
        int carry = 0;
        while (l1Iter != null || l2Iter != null) {
            int curNum = 0;
            ListNode newNode = new ListNode();
            if (l1Iter != null) {
                curNum += l1Iter.val;
                l1Iter = l1Iter.next;
            }
            if (l2Iter != null) {
                curNum += l2Iter.val;
                l2Iter = l2Iter.next;
            }
            newNode.val = (curNum + carry) % 10;
            carry = (curNum + carry) / 10;
            resultIter.next = newNode;
            resultIter = resultIter.next;
        }
        if (carry > 0) {
            resultIter.next = new ListNode(carry);
        }
        return result.next;
    }
}