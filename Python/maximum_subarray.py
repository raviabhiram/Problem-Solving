"""
Author: Abhiram Ravi Bharadwaj
Source: Leetcode
Problem: https://leetcode.com/problems/maximum-subarray/
"""
import math

def main(a):
	local_max = -math.inf
	global_max = -math.inf
	for i in range(len(a)):
		local_max = max(a[i], local_max + a[i])
		global_max = max(global_max, local_max)
	return global_max

if __name__ == '__main__':
	print(main([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
