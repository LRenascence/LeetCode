"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        bfsList = [(root, 0)]
        res = []
        index = -1
        while bfsList:
            curNode, curLv = bfsList.pop(0)
            if curNode:
                if curLv == index:
                    res[-1].append(curNode.val)
                else:
                    res.append([])
                    index += 1
                    res[-1].append(curNode.val)
                bfsList.append((curNode.left, curLv + 1))
                bfsList.append((curNode.right, curLv + 1))
        return res