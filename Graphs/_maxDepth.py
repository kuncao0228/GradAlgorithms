"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root is None:
            return 0
        
        
        depth = 1
        for i in range(len(root.children)):
            tempRoot = root.children[i]
            traverseDepth = self.maxDepth(tempRoot)
            depth = max(depth, traverseDepth + 1)
        
        
        return depth
            
        

        