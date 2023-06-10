package besttimebuysellstock4

import "math"

func maxProfit(k int, prices []int) int {
	pricesLen := len(prices)
	if k >= pricesLen / 2 {
		profit := 0
		for i := 1; i < pricesLen; i++ {
			if prices[i] > prices[i-1] {
				profit += prices[i] - prices[i-1]
			}
		}
		return profit
	}
	dp := make([][]int, k+1)
	for i := range dp {
		dp[i] = make([]int, pricesLen)
	}
	for i := 1; i <= k; i++ {
		tmpMax := -prices[0]		
		for j := 1; j < pricesLen; j++ {
			dp[i][j] = int(math.Max(float64(dp[i][j-1]), float64(prices[j] + tmpMax)))
			tmpMax = int(math.Max(float64(tmpMax), float64(dp[i-1][j-1] - prices[j])))
		}
	}
	return dp[k][pricesLen - 1]
}
