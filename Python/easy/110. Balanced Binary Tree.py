"""
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
Example 1:
Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.
Example 2:
Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
"""
class Solution:
    def isBalanced(self, root: 'TreeNode') -> 'bool':
        self.maxHeightDiff = 0
        self.getHeight(root)
        if self.maxHeightDiff > 1:
            return False
        else:
            return True
    def getHeight(self, root):
        if not root:
            return 0
        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)
        curHeightDiff = abs(leftHeight - rightHeight)
        if curHeightDiff > self.maxHeightDiff:
            self.maxHeightDiff = curHeightDiff
        return max(leftHeight, rightHeight) + 1