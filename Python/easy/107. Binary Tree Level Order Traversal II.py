"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursive solution
class Solution:
    def levelOrderBottom(self, root: 'TreeNode') -> 'List[List[int]]':
        self.rList = []
        self.searchTree(root, 0)
        return self.rList

    def searchTree(self, root, level):
        if not root:
            return None
        if level >= len(self.rList):
            self.rList.insert(0, [])
        self.rList[-level - 1].append(root.val)
        self.searchTree(root.left, level + 1)
        self.searchTree(root.right, level + 1)
        return None

# DFS + stack solution
class Solution:
    def levelOrderBottom(self, root: 'TreeNode') -> 'List[List[int]]':
        if not root:
            return []
        nodeStack = []
        nodeStack.append((root, 0))
        rList = []
        while nodeStack:
            curNode, curLevel = nodeStack.pop()
            if curLevel >= len(rList):
                rList.insert(0, [])
            rList[-curLevel - 1].append(curNode.val)
            if curNode.right:
                nodeStack.append((curNode.right, curLevel + 1))
            if curNode.left:
                nodeStack.append((curNode.left, curLevel + 1))
        return rList

# BFS + queue solution
class Solution:
    def levelOrderBottom(self, root: 'TreeNode') -> 'List[List[int]]':
        if not root:
            return []
        nodeQueue = []
        nodeQueue.append((root, 0))
        rList = []
        while nodeQueue:
            curNode, curLevel = nodeQueue.pop(0)
            if curLevel >= len(rList):
                rList.insert(0, [])
            rList[-curLevel - 1].append(curNode.val)
            if curNode.left:
                nodeQueue.append((curNode.left, curLevel + 1))
            if curNode.right:
                nodeQueue.append((curNode.right, curLevel + 1))
        return rList