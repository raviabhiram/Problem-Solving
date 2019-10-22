"""
Author: Abhiram Ravi Bharadwaj
Source: Leetcode
Problem: https://leetcode.com/problems/string-to-integer-atoi/
"""

def atoi(s):
	s = s.lstrip()
	if s == '':
		return 0
	product = 1
	if s[0] == '-':
		product = -1
		s = s[1:]
	elif s[0] == '+':
		s = s[1:]
	num = 0
	while s and ord('9') >= ord(s[0]) >= ord('0'):
		num = (num * 10) + int(s[0])
		s = s[1:]
	num *= product
	if num < -2 ** 31:
		return -2 ** 31
	if num > 2 ** 31 - 1:
		return 2 ** 31 - 1
	return num

def main():
	print(atoi("   -42abc"))

if __name__ == '__main__':
	main()
