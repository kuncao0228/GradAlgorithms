class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        
        for i in range(len(A)):
            p1 = 0
            p2 = len(A[i]) - 1
            
            while p2 >= p1:
                
                
                A[i][p1], A[i][p2] = A[i][p2], A[i][p1]
                p2 -= 1
                p1 += 1
        
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    A[i][j] = 0
                else:
                    A[i][j] = 1
        
        
        return A
                
        