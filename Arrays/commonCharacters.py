class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        tempSet = []

        if len(A) == 0:
            return tempSet
        
        for i in range(len(A[0])):
            tempSet.append(A[0][i])
            
        if len(A) == 1:
            return tempSet
        
        for i in range(1, len(A)):
            retSet = []
            for j in range(len(A[i])):
                if A[i][j] in tempSet:
                    retSet.append(A[i][j])
                    tempSet.remove(A[i][j])
            
            tempSet = retSet