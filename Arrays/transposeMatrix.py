class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        retList = []
        if len(A) < 1:
            return retList
        
        
        for i in range(len(A[0])):
            tempList = []
            for j in range(len(A)):
                tempList.append(A[j][i])
            
            retList.append(tempList)
        
        return retList
                