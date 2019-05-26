class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        dp = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        if len(matrix) == 0:
            return 0
        
        if len(matrix) == 1:
            for i in range(len(matrix[0])):
                if matrix[0][i] == "1":
                    return 1
                
        if len(matrix[0]) == 1:
            for i in range(len(matrix)):
                if matrix[i][0] == "1":
                    return 1
        
        
        for i in range(len(matrix[0])):
            if matrix[0][i] == "1":
                dp[0][i] = 1
        
        for i in range(len(matrix)):
            if matrix[i][0] == "1":
                dp[i][0] = 1
                
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == "1":
                    dp[i][j] = 1
                
                if dp[i-1][j] != 0 and dp[i][j-1] != 0 and dp[i-1][j-1] != 0 and matrix[i][j] == "1":
                    dp[i][j] = min(min(dp[i][j-1],dp[i-1][j-1]),dp[i-1][j]) + 1

        side = max(map(max, dp))
        return side * side
        
        