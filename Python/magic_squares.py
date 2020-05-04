"""
Author: Abhiram Ravi Bharadwaj
Source: HackerRank
Problem: https://www.hackerrank.com/challenges/magic-square-forming/problem
"""
from itertools import permutations, chain

def main():
	matrix = [[4, 5, 8], [2, 4, 1], [1, 9, 7]]
	input = list(chain.from_iterable(matrix))
	cost = 999
	for perm in permutations(range(1, 10)):
		if (sum(perm[0:3]) == sum(perm[3:6]) == sum(perm[6:9]) == 15 and
			sum(perm[0::3]) == sum(perm[1::3]) == 15 and
			perm[0] + perm[4] + perm[8] == 15 and
			perm[2] + perm[4] + perm[6] == 15
		):
			cost = min(cost, sum([abs(input[i]-perm[i]) for i in range(9)]))
	print(cost)
	return cost

if __name__ == '__main__':
	main()
