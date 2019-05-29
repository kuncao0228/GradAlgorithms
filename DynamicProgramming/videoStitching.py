class Solution(object):
    def videoStitching(self, clips, T):
        """
        :type clips: List[List[int]]
        :type T: int
        :rtype: int
        """
        
        dp = [0] * (T+1)
        
        clips = sorted(clips, key=lambda x: x[0])
        
        for clip in clips:
            if clip[0] == 0:
                for i in range(clip[0], min(T+1, clip[1]+1)):
                    dp[i] = 1
            
            else:
                if dp[min(clip[0], T)] != 0:
                    minimum = 1000
                    for j in range(clip[0], min(clip[1] + 1, T+1)):
                        if dp[j] < minimum and dp[j] != 0:
                            minimum = dp[j]
                    for j in range(clip[0], min(clip[1] + 1, T+1)):
                        
                        if dp[j] != 0:
                            dp[j] = min(dp[j], minimum + 1)
                        else:
                            dp[j] = minimum + 1
            
            
        if dp[T] == 0:
            return -1
        
        return (dp[T])
                    
                    
            
        