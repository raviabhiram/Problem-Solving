"""
Author: Abhiram Ravi Bharadwaj
Source: Leetcode
Problem: https://leetcode.com/problems/valid-palindrome
"""

def isPalindrome(s):
	t = [ch.lower() for ch in s if ch.isalnum()]
	i = 0
	while i < len(t) - i - 1:
		if t[i] != t[len(t) - i - 1]:
			return False
	return True

def main():
	isPalindrome("A man, a plan, a canal: Panama")

if __name__ == '__main__':
	main()
