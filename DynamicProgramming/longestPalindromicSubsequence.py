class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        
        if len(s) < 2:
            return len(s)
        
        dp = [[0 for col in range(len(s))] for row in range(len(s))]
        
        for i in range(len(dp)):
            dp[i][i] = 1
        
        
        for length in range(1,len(s)):    
            for start in range(len(s)):
                end = start + length
                if end < len(s):
                    if s[start] == s[end]:
                        dp[start][end] = dp[start+1][end-1] + 2
                    else:
                        dp[start][end] = max(dp[start][end-1], dp[start+1][end])
                        
        
        return dp[0][len(dp[0])-1]
                