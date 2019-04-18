class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [nums[0]]
      
        for i in range(1,len(nums)): 
            dp.append(max(nums[i], dp[i-1] + nums[i]) )
            
        return max(dp) 
        