"""
Author: Abhiram Ravi Bharadwaj
Source: Leetcode
Problem: https://leetcode.com/problems/interleaving-string/
"""

def maxArea(h, w, horizontalCuts, verticalCuts):
	maxH = maxW = 0
	horizontalCuts.sort()
	verticalCuts.sort()
	horizontalCuts = [0] + horizontalCuts + [h]
	verticalCuts = [0] + verticalCuts + [w]

	for i in range(1, len(horizontalCuts)):
		maxH = max(maxH, horizontalCuts[i] - horizontalCuts[i - 1])
	for i in range(1, len(verticalCuts)):
		maxW = max(maxW, verticalCuts[i] - verticalCuts[i - 1])
	return (maxH * maxW) % ((10 ** 9) + 7)

def main():
	print(maxArea(5, 4, [1, 2, 4], [1, 3]))

if __name__ == '__main__':
	main()