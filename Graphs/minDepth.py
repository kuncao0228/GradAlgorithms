# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        
        """
    
        if root == None:
            return 0
        
        if root.left == None and root.right == None:
            return 1
        
        
        
        leftDepth = self.minDepth(root.left) + 1
        rightDepth =self.minDepth(root.right) + 1

        if leftDepth == 1:
            return rightDepth
        if rightDepth == 1:
            return leftDepth
        
        return min(leftDepth, rightDepth)
        
        