"""
Author: Abhiram Ravi Bharadwaj
Source: Leetcode
Problem: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""

def letterCombination(digits):
	if digits == "":
		return []
	num_map = {
		'2': ['a', 'b', 'c'],
		'3': ['d', 'e', 'f'],
		'4': ['g', 'h', 'i'],
		'5': ['j', 'k', 'l'],
		'6': ['m', 'n', 'o'],
		'7': ['p', 'q', 'r', 's'],
		'8': ['t', 'u', 'v'],
		'9': ['w', 'x', 'y', 'z']
	}
	res = num_map[digits[0]]
	for i in range(1, len(digits)):
		new_res = []
		for s in res:
			for letter in num_map[digits[i]]:
				new_res.append(s + letter)
		res = new_res
	return res

def main():
	print(letterCombination('23'))

if __name__ == '__main__':
	main()