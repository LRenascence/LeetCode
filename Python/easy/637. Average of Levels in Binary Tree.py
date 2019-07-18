"""
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        nodeList = [(root, 0)]
        curLv = 0
        resultList = []
        sameLvNum = []
        while nodeList:
            (curNode, curNodeLv) = nodeList.pop(0)
            if curNode.left:
                nodeList.append((curNode.left, curNodeLv + 1))
            if curNode.right:
                nodeList.append((curNode.right, curNodeLv + 1))
            if curLv == curNodeLv:
                sameLvNum.append(curNode.val)
            else:
                resultList.append(sum(sameLvNum) / len(sameLvNum))
                sameLvNum = [curNode.val]
                curLv += 1
        resultList.append(sum(sameLvNum) / len(sameLvNum))
        return resultList