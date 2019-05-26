class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        retSum = 0
        
        for i in range(0, len(nums), 2):
            retSum += min(nums[i],nums[i+1])
            
        return retSum
        