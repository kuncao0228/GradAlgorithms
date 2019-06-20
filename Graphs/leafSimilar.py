# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        array1 = self.helper(root1, [])
        array2 = self.helper(root2, [])
        
        print array1
        print array2
        
        if array1 == array2:
            return True
        return False
        
    def helper(self,root, array):
        
        if root == None:
            return array
        
        if root.right == None and root.left == None:
            array.append(root.val)
        
        if root.right != None:
            self.helper(root.right, array)

        if root.left != None:
            self.helper(root.left, array)
        
        return array