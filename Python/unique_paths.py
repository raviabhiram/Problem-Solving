"""
Author: Abhiram Ravi Bharadwaj
Source: Leetcode
Problem: https://leetcode.com/problems/unique-paths/
"""

def solve(m, n):
	sol = [[0 for i in range(n + 1)] for j in range(m + 1)]
	sol[1][1] = 1
	print(sol)
	for i in range(1, m + 1):
		for j in range(1, n + 1):
			sol[i][j] += sol[i][j - 1] + sol[i - 1][j]
	return sol[m][n]


def main():
	print(solve(m=3, n=7))

if __name__ == '__main__':
	main()