class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        
        total = sum(nums)
        if abs(S) > total or (S + total) % 2 != 0:
            return 0
            

        dp = [[0 for col in range(2 * sum(nums) + 1)] for row in range(len(nums) + 1)]
        dp[0][sum(nums)] = 1
        
        
        
        for i in range(1,len(dp)):
            for j in range(len(dp[0])):
                if dp[i-1][j] != 0:
                    dp[i][j - nums[i-1]] += dp[i-1][j]
                    dp[i][j + nums[i-1]] += dp[i-1][j]
                    
        
        
        return dp[len(dp)-1][S + sum(nums)]
        