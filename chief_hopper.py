"""
Author: Abhiram Ravi Bharadwaj
Source: HackerRank
Problem Link: https://www.hackerrank.com/challenges/chief-hopper/problem
"""
import math

def solve(n, b):
	new_energy = 0
	for num in b[::-1]:
		new_energy = math.ceil((new_energy + num) / 2)
	return new_energy

def main():
	n = 3
	b = [1, 6, 4]
	print(solve(n, b))

if __name__ == '__main__':
	main()
