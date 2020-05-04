"""
Author: Abhiram Ravi Bharadwaj
Source: Leetcode
Problem: https://leetcode.com/problems/trapping-rain-water/
"""

def trap(height):
	l = 0
	r = len(height)-1
	i = 0
	j = len(height) - 1
	count = 0
	while i < j:
		if height[i] < height[j]:
			updated = 'i'
		else:
			updated = 'j'
		if updated == 'i':
			if height[i] < height[l]:
				count += height[l] - height[i]
			else:
				l = i
			i += 1
		else:
			if height[j] < height[r]:
				count += height[r] - height[j]
			else:
				r = j
			j -= 1
	return count

def main():
	print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
	# print(trap([4, 2, 3]))

if __name__ == '__main__':
	main()
