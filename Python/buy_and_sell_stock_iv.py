"""
Author: Abhiram Ravi Bharadwaj
Source: Leetcode
Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
"""
import math

def maxProfit(k, prices):
	if len(prices) <= 1 or k < 1:
		return 0
	if k >= len(prices) // 2:
		profit = 0
		for i in range(1, len(prices)):
			if prices[i] > prices[i - 1]:
				profit += prices[i] - prices[i - 1]
		return profit
	k = min(k, len(prices) // 2)
	dp = [[0 for i in range(len(prices))] for j in range(k + 1)]
	for i in range(1, k + 1):
		max_profit = -math.inf
		for j in range(1, len(prices)):
			max_profit = max(max_profit, dp[i - 1][j - 1] - prices[j - 1])
			dp[i][j] = max(dp[i][j - 1], max_profit + prices[j])
	return dp[k][len(prices) - 1]

def main():
	print(maxProfit(2, [3, 2, 6, 5, 0, 3]))
	print(maxProfit(2, [2,4,1]))

if __name__ == '__main__':
	main()
