class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        temp = sorted(heights)
        count = 0
        for i in range(0,len(heights)):
            if temp[i] != heights[i]:
                count += 1
        
        return count