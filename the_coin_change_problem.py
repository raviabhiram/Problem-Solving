"""
Author: Abhiram Ravi Bharadwaj
Source: Hackerrank
Problem: https://www.hackerrank.com/challenges/coin-change/problem
"""
def solve(n, c):
	if n == 0:
		return 0
	dp = [0] * (n + 1)
	dp[0] = 1
	for coin in c:
		for i in range(coin, n + 1):
			dp[i] = dp[i - coin] + dp[i]
	return dp[n]

def main():
	n, m = 4, 3
	c = [1, 2, 3]
	print(solve(n, c))

if __name__ == '__main__':
	main()
