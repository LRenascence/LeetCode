"""
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.sum = 0
    def convertBST(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None
        self.convertBST(root.right)
        root.val += self.sum
        self.sum = root.val
        self.convertBST(root.left)
        return root