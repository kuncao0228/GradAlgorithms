class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n == 0 :
            return 1
        
        dp = [0] * (n + 1)
        dp[1] = 10
        
        for i in range(2,n+1):
            factor = 8
            nonRepeat = 9*9
            for j in range(i-2):
                nonRepeat *= factor
                factor -= 1
            
            dp[i] = dp[i-1] + nonRepeat
        
        return(dp[n])
                
                
            