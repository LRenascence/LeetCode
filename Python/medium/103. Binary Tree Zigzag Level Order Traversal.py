"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# iterative solution
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        nodeList = [(root, 0)]
        res = []
        # True is left to right, False is right to left
        zigzag = False
        index = -1
        while nodeList:
            curNode, curLv = nodeList.pop(0)
            if not curNode:
                continue
            if curLv != index:
                index += 1
                res.append([])
                zigzag = not zigzag
            if zigzag:
                res[-1].append(curNode.val)
            else:
                res[-1].insert(0, curNode.val)
            nodeList.append((curNode.left, curLv + 1))
            nodeList.append((curNode.right, curLv + 1))
        return res

# recursive solutino
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        nodeList = [(root, 0)]
        res = []
        # True is left to right, False is right to left
        zigzag = True
        def dfs(root, level, zigzag):
            if not root:
                return 0
            if level == len(res):
                res.append([])
            if zigzag:
                res[level].append(root.val)
            else:
                res[level].insert(0, root.val)
            dfs(root.left, level + 1, not zigzag)
            dfs(root.right, level + 1, not zigzag)
            return 0
        dfs(root, 0, zigzag)
        return res