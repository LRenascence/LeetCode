"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursive solution
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def inorder(root):
            if not root:
                return 0
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        return res

# iterative solution, use stack
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        nodeList = []
        curNode = root
        while curNode or nodeList:
            while curNode:
                nodeList.append(curNode)
                curNode = curNode.left
            curNode = nodeList.pop()
            res.append(curNode.val)
            curNode = curNode.right
        return res
            