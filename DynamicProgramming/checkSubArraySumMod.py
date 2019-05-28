class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        
        
        
        """
        
        if len(nums) < 2:
            return False

        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = dp[0] + nums[1]
        
        if k != 0:
            if dp[1] % k == 0:
                return True
        else:
            if dp[0] == 0 and dp[1] == 0:
                return True
        
        for i in range(2, len(dp)):
            dp[i] = dp[i-1] + nums[i]
            if k != 0 and dp[i] % k == 0:
                return True
            elif k == 0 and dp[i] == 0:
                return True
            
            for j in range(i-2, -1,-1):
                temp = dp[i] - dp[j]
                if k !=0 and temp % k == 0:
                    return True
                elif k==0 and temp == 0:
                    return True
        

                       

        return False
                    
        