class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.dp = []
        sum = 0
        
        for i in range(0, len(nums)):
            sum += nums[i]
            self.dp.append(sum)
            
        
        print(self.dp)
            
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.dp[j]       
        return self.dp[j] - self.dp[i-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)