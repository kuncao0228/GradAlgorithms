class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        
        if len(prices) < 2:
            return 0
        
        retProfit = 0;
        buy = prices[0]
        
        
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] > buy + fee:
                retProfit += prices[i] - fee - buy
                buy = prices[i] - fee
        
        return retProfit
        