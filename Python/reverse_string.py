"""
Author: Abhiram Ravi Bharadwaj
Source: Leetcode
Problem: https://leetcode.com/problems/reverse-string/
"""
def reverse_string(s):
	for i in range(len(s) // 2):
		s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]

def main():
	s = ["h", "e", "l", "l", "o"]
	reverse_string(s)
	print(s)

if __name__ == '__main__':
	main()
