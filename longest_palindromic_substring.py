"""
Author: Abhiram Ravi Bharadwaj
Source: Leetcode
Problem: https://leetcode.com/problems/longest-palindromic-substring/
"""
def longest_palindrome(s):
	if s == "":
		return s
	length = len(s)
	for i in range(length, 1, -1):
		for j in range(length):
			k = i + j
			if k > length:
				break
			substring = s[j:k]
			if substring == substring[::-1]:
				return substring
	return s[0]

def main():
	print(longest_palindrome('babad'))

if __name__ == '__main__':
	main()