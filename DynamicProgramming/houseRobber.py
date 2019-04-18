class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        dp = []
        
        #Checks
        if (len(nums) >= 2):
            dp.append(nums[0])
            dp.append(max(nums[0], nums[1]))       
        if len(nums) == 2:
            return max(nums[0],nums[1])
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 0:
            return 0

        
        for i in range(2,len(nums)):
            dp.append(max(nums[i] + dp[i-2], dp[i-1]))
        
        
        return dp[len(nums)-1]