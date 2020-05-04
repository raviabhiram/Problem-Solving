"""
Author: Abhiram Ravi Bharadwaj
Source: CodeChef
Problem: https://www.codechef.com/problems/MARBLES
"""

def choose(n, r):
	options = 1
	r = min(r, n - r)
	for i in range(r):
		options = options * (n - i) / (1 + i)
	return options

def main():
	for test in range(int(input())):
		n, k = map(int, input().split())
		print(int(choose(n - 1, k - 1)))  # https://en.wikipedia.org/wiki/Combination#Number_of_combinations_with_repetition

if __name__ == '__main__':
	main()
