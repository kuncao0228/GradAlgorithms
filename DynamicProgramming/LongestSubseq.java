class Solution {
    public int lengthOfLIS(int[] nums) {
        
        if(nums.length == 0){
            return 0;
        }
        
        int dp[] = new int[nums.length];
        int ret = -1;
               
        dp[0] = 1;
        for (int i = 0; i < nums.length; i ++){
            dp[i] = 1;
            for (int j = 0; j < i; j ++){
                if (nums[i] > nums[j] && dp[i] < dp[j] + 1){
                    dp[i] = dp[j] + 1;
                }
            }         
        }
        
        for (int i = 0; i < dp.length; i ++){
            System.out.println(dp[i]);
            if (dp[i] > ret){
                ret = dp[i];
            }
        }
        
        return ret;        
    }
}