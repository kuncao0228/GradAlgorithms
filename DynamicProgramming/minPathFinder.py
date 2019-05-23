class Solution(object):
    def minFallingPathSum(self, A):
        while len(A) >= 2:
            row = A.pop()  
            for i in range(len(row)):                
                if(i == 0):
                    A[-1][i] += min(row[i], row[i+1])
                elif(i == len(row)-1):  
                    A[-1][i] += min(row[i], row[i-1])
                else:
                    A[-1][i] += min(row[i-1:i+2])
                
        return min(A[0])