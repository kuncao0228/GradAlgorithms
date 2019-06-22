# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        
        if root == None:
            return 0
        
        retList = []      
        queue = [root]
        
        while len(queue) > 0:
            nextQueue = []
            for node in queue:
                if node.val >= L and node.val <= R:
                    retList.append(node.val)
                
                
                if node.left and node.val >= L:
                    nextQueue.append(node.left)
                
                if node.right and node.val <= R:
                    nextQueue.append(node.right)
            
            queue = nextQueue
        
        return sum(retList)
                
                    
            
            
        
        