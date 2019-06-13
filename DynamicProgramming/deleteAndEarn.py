class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        
        temp = [0] * 100001
        dp = [0] * 100001
           
        for i in range(len(nums)):
            temp[nums[i]] += nums[i]
            
        dp[0] = temp[0]
        dp[1] = temp[1]
        dp[2] = max(temp[1], temp[2])
        
        for i in range(2,len(dp)):
            dp[i] = max(temp[i] + dp[i-2], dp[i-1])
        

        return dp[len(dp)-1]
        
        