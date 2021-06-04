"""
Author: Abhiram Ravi Bharadwaj
Source: Leetcode
Problem: https://leetcode.com/problems/3sum/
"""

def solve(nums):
	answer = []
	nums = sorted(nums)
	for i in range(len(nums) - 2):
		if i > 0 and nums[i] == nums[i - 1]:
			continue
		j = i + 1
		k = len(nums) - 1
		while j < k:
			curr_sum = nums[i] + nums[j] + nums[k]
			if curr_sum == 0:
				answer.append([nums[i], nums[j], nums[k]])
				j += 1
				while j < k and nums[j] == nums[j - 1]:
					j += 1
			elif curr_sum < 0:
				j += 1
			else:
				k -= 1
	return answer

def main():
	print(solve([-1, 1, 0, -1, 2]))

if __name__ == '__main__':
	main()
