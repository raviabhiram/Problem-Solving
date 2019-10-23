"""
Author: Abhiram Ravi Bharadwaj
Source: Leetcode
Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""
import sys
def maxProfit(prices):
	l = sys.maxsize
	profit = 0
	for i in range(len(prices)):
		if prices[i] < l:
			l = prices[i]
		elif prices[i] - l > profit:
			profit = prices[i] - l
	return profit

def main():
	print(maxProfit([7,1,5,3,6,4]))

if __name__ == '__main__':
	main()