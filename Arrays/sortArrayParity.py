class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        p1 = 0
        p2 = len(A) - 1 
        
        while p2 > p1:
            if A[p2] % 2 < A[p1] % 2:
                temp = A[p2]
                A[p2] = A[p1]
                A[p1] = temp
            
            if A[p1] % 2 == 0:
                p1 += 1
            if A[p2] %2 == 1:
                p2 -= 1
        
        return A
            
        