class Solution(object):
    def mincostTickets(self, days, costs):
        dp = [sys.maxint] * 366        
        dp[0] = 0;       
        for i in range(1, len(dp)):
            
            if i not in days:
                dp[i] = dp[i-1]
                continue
            
            dp[i] = dp[i-1] + min(costs)
            
            if i >= 7:
                dp[i] = min(dp[i], dp[i-7] + costs[1])
            else:
                dp[i] = min(dp[i], costs[1])
 
            if i >= 30:
                dp[i] = min(dp[i], dp[i-30] + costs[2])
        
            else:
                dp[i] = min(dp[i], costs[2])
                
        return dp[len(dp)-1]