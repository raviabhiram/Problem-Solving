"""
Author: Abhiram Ravi Bharadwaj
Source: HackerRank
Problem Link: https://www.hackerrank.com/challenges/kmp-problem/problem
"""
import math

def solve(counts):
	smallest_char = None
	second_smallest_char = None
	min = math.inf
	min_index = -1

	# Find the index with lowest frequency, the smallest character and second smallest character.
	for i in range(len(counts)):
		if 0 < counts[i] < min:
			if smallest_char is None:
				smallest_char = i
			if second_smallest_char is None and smallest_char is not None:
				second_smallest_char = i
			min = counts[i]
			min_index = i
	S = chr(ord('a') + min_index)  # Begin the string with lowest frequency.
	counts[min_index] -= 1

	# Add all letters until the letter with lowest frequency.
	for i in range(min_index):
		S += (chr(ord('a') + i) * counts[i])
	next = min_index

	# If the character with lowest frequency is also the smallest, interleave it with the next smallest character.
	# This is done to ensure the lowest cost and lexographically smallest.
	if min_index == smallest_char and counts[min_index] > 0:
		next = min_index + 1
		while next < 26 and counts[next] == 0:
			next += 1
		if next < 26:
			while counts[min_index] > 0:
				S += (chr(ord('a') + min_index) + chr(ord('a') + next))
				counts[min_index] -= 1
				counts[next] -= 1
		else:
			next = min_index

	# For all the remaining characters or if the previous condition fails, add them in order.
	for i in range(next, len(counts)):
		S += (chr(ord('a') + i) * counts[i])
	return S

def main():
	counts = list(map(int, input().strip().split()))
	print(solve(counts))

if __name__ == '__main__':
	main()
