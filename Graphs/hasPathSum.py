# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, summation):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        
        if root == None:
            return False
            
        
        if root.left == None and root.right == None:
            summation -= root.val
            if summation == 0:
                return True
            else:
                return False
            
        
        summation -= root.val
        
        left = False
        right = False
        
        if root.left != None:
            left = self.hasPathSum(root.left, summation)
        
        if root.right != None:
            right = self.hasPathSum(root.right, summation)
            
        return left or right
        
        
        