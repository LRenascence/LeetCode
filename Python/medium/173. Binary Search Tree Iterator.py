"""
initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

 

Example:



BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false
 

Note:

next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.nodeList = []
        def inorder(root):
            if not root:
                return None
            inorder(root.left)
            self.nodeList.append(root.val)
            inorder(root.right)
            return None
        inorder(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.nodeList.pop(0)
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return True if self.nodeList else False


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.nodeStack = []
        while root:
            self.nodeStack.append(root)
            root = root.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        curNode = self.nodeStack.pop()
        newNode = curNode.right
        if newNode:
            while newNode:
                self.nodeStack.append(newNode)
                newNode = newNode.left
        return curNode.val
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return True if self.nodeStack else False
