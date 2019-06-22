# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helperMean(self, meanList):
        summation = 0
        for node in meanList:
            summation += node.val
        
        return (float)(summation)/len(meanList)
            
        
    
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        
        if root == None:
            return []
        
        retList = []
        
        queue = [root]
        while len(queue) > 0:
            nextQueue = []
            for node in queue:
                if node.left:
                    nextQueue.append(node.left)
                
                if node.right:
                    nextQueue.append(node.right)
            
            retList.append(self.helperMean(queue))
            queue = nextQueue
        
        return retList
            
            
                    
            
        
        
            

        
        