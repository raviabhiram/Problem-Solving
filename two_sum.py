"""
Author: Abhiram Ravi Bharadwaj
Source: Leetcode
Problem: https://leetcode.com/problems/two-sum/
"""
def twoSum(self, nums, target: int):
	diff = {}
	for i in range(len(nums)):
		if nums[i] in diff:
			return [diff[nums[i]], i]
		diff[target - nums[i]] = i

def main():
	print(twoSum([2, 7, 11, 15], 9))

if __name__ == '__main__':
	main()