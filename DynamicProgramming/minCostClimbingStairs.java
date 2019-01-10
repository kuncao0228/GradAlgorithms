class Solution {
    public int minCostClimbingStairs(int[] cost) {
              
        int dp [] = new int[cost.length];       
        dp[0] = cost[0];
        dp[1] = cost[1];
        
        for (int i = 2; i < cost.length; i++ ){
            dp[i] = cost[i];
            
            if(dp[i] + dp[i-1] > dp[i] + dp[i-2]){
                dp[i] += dp[i-2];
            }
            else{
                dp[i] += dp[i-1];
            }           
        }
            
        for (int i = 0; i < dp.length; i ++){
            System.out.println(dp[i]);
        }
        return Math.min(dp[cost.length-1], dp[cost.length-2]);
        
    }
}