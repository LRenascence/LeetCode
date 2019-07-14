"""
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        # find the t root
        nodeList = [s]
        tRootList = []
        while nodeList:
            curNode = nodeList.pop()
            if curNode:
                if curNode.val == t.val:
                    tRootList.append(curNode)
                nodeList.append(curNode.left)
                nodeList.append(curNode.right)
        if not tRootList:
            return False
        # check if is subtree
        for root in tRootList:
            if self.isSame(root, t):
                return True
        return False

    def isSame(self, s, t):
        if s and t:
            return self.isSame(s.left, t.left) and self.isSame(s.right, t.right) and s.val == t.val
        if s or t:
            return False
        return True


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s is None:
            return False
        if self.isSame(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isSame(self, s, t):
        if s and t:
            return self.isSame(s.left, t.left) and self.isSame(s.right, t.right) and s.val == t.val
        if s or t:
            return False
        return True

