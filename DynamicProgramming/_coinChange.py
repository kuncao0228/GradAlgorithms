class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        if amount == 0:
            return 0
        
        dp = [0]
        for _ in range(1, amount+1):
            dp.append(amount+1)

        for coin in coins:
            for current_amount in range(coin, amount+1):
              dp[current_amount] = min(dp[current_amount], dp[current_amount - coin] + 1)
        

        if dp[amount] > amount:
            return -1
        return dp[amount]
        