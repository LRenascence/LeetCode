"""
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:

Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True


Example 2:

Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        nodeList = [root]
        numDict = {}
        while nodeList:
            curNode = nodeList.pop(0)
            if curNode:
                sub = k - curNode.val
                if curNode.val in numDict:
                    return True
                else:
                    numDict[sub] = curNode.val
                nodeList.append(curNode.left)
                nodeList.append(curNode.right)
        return False