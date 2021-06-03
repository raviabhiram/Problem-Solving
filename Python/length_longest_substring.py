"""
Author: Abhiram Ravi Bharadwaj
Source: Leetcode
Problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""

def solve(s):
	if len(s) < 2:
		return len(s)
	seen = {}
	result = 0
	start = 0
	for i in range(len(s)):
		if s[i] in seen and seen[s[i]] >= start:
			start = seen[s[i]] + 1
		result = max(result, i - start + 1)
		seen[s[i]] = i
	return result

def main():
	s = "abcdab"
	print(solve(s))

if __name__ == '__main__':
	main()