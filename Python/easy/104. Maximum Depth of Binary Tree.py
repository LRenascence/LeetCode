"""
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Note: A leaf is a node with no children.
Example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursive solution
class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self.findMaxDepth(root, 1)

    def findMaxDepth(self, root, count):
        if not root.left and not root.right:
            return count
        if not root.left:
            return self.findMaxDepth(root.right, count + 1)
        if not root.right:
            return self.findMaxDepth(root.left, count + 1)
        return max(self.findMaxDepth(root.left, count + 1), self.findMaxDepth(root.right, count + 1))

# simple recursive solution
class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        else:
            leftHeight = self.maxDepth(root.left)
            rightHeight = self.maxDepth(root.right)
            return max(leftHeight, rightHeight) + 1