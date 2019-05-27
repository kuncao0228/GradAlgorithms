class Solution(object):
    def longestArithSeqLength(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        

        dp = []
        dp.append({})

        
        retMax = 0;
        
        for i in range(1, len(A)):
            dictionary = {}
            for j in range(i-1, -1, -1):
                diff = A[i] - A[j]  
                
                if diff in dp[j]:
                    if diff not in dictionary:
                        dictionary[diff] = dp[j][diff] + 1
                    else:
                        dictionary[diff] = max(dictionary[diff], dp[j][diff] + 1)
                        
                if diff not in dictionary:
                    dictionary[diff] = 2
            
            dp.append(dictionary)     

            tempMax = max(dictionary.values())
            if tempMax > retMax:
                retMax = tempMax
            
        return retMax
            
            
            