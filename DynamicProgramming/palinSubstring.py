def isPal(input):
    if input == input[::-1]:
        return True
    
    return False



class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0] * (len(s)+1)
        
        for i in range(0,len(s)):
            dp[i+1] = dp[i]

            
            
            for j in range(i,-1,-1):
                subString = s[j:i+1]
                if isPal(subString) and len(subString) > 0:
                    dp[i+1] += 1
            
        return dp[len(dp)-1]
    
        
            
        