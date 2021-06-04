"""
Author: Abhiram Ravi Bharadwaj
Source: Leetcode
Problem: https://leetcode.com/problems/3sum-closest/
"""

import math

def solve(nums, target):
	nums.sort()
	diff = math.inf
	for i in range(len(nums)):
		j, k = i + 1, len(nums) - 1
		while j < k:
			curr_sum = nums[i] + nums[j] + nums[k]
			if curr_sum == target:
				return curr_sum
			if abs(target - curr_sum) < abs(diff):
				diff = target - curr_sum
			if curr_sum < target:
				j += 1
			else:
				k -= 1
	return target - diff

def main():
	print(solve([-1, 1, 2, -4], 1))

if __name__ == '__main__':
	main()
