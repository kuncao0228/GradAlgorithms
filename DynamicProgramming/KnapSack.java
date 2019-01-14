
import java.util.*;


public class KnapSack{
	public static void main(String[] args){
		int[] weight = {1,3,4,5};
		int[] value = {1,4,5,7};


		System.out.println(maxValue(weight, value, 7));

	}

	public static int maxValue(int[] weight, int[] value, int maxWeight){

		int dp[][] = new int[weight.length+1][maxWeight+1];


		for  (int i = 0; i < dp.length; i++){


			for (int w = 0; w < dp[0].length; w++){

				if(w == 0 || i == 0){
					dp[i][w] = 0;
				}


				else if(w <= maxWeight && w-weight[i-1] >= 0){

					dp[i][w] = Math.max(dp[i-1][w-weight[i-1]] + value[i-1], dp[i-1][w]);

				}
				else{
					dp[i][w] = dp[i-1][w];
				}
			}
		}


		for (int i = 0; i < dp.length; i ++){
			for (int j = 0; j < dp[0].length; j ++){
				System.out.print(dp[i][j] + " ");
			}
			System.out.println("\n");
		}



		return dp[dp.length-1][dp[0].length-1];

	}
}