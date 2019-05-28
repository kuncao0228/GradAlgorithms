class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        
        dp = [[0 for col in range(len(obstacleGrid[0]))] for row in range(len(obstacleGrid))]
        
        noObs = True
        
        if len(obstacleGrid) == 0:
            return 0
        if len(obstacleGrid) == 1 or len(obstacleGrid[0]) == 1:
            if any(1 in sublist for sublist in obstacleGrid):
                return 0
            else:
                return 1
        
        
        for i in range(len(obstacleGrid)):
            if noObs and obstacleGrid[i][0] == 0:
                dp[i][0] = 1
            else:
                dp[i][0] = 0
                noObs = False
                
        noObs = True
        for i in range(len(obstacleGrid[0])):
            if noObs and obstacleGrid[0][i] == 0:
                dp[0][i] = 1
            else:
                dp[0][i] = 0
                noObs = False
                
        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                else:
                    dp[i][j] = 0
        
        return dp[len(dp) - 1][len(dp[0]) - 1]
            
        
