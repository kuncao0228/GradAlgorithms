class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        profit = 0;
        buy = sys.maxsize
        
        for i in range(len(prices)):
            if prices[i] < buy:
                buy = prices[i]

            
            if prices[i] > buy and  prices[i] - buy > profit:
                profit = prices[i] - buy

        
        
        return profit
                
            