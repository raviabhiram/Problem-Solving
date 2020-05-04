"""
Author: Abhiram Ravi Bharadwaj
Source: Leetcode
Problem: https://leetcode.com/problems/valid-parentheses/
"""
def valid_paranthesis(s):
	seen = []
	match = {
		'{': '}',
		'[': ']',
		'(': ')'
	}
	for ch in s:
		if ch in match:
			seen.append(ch)
		else:
			if not seen or match[str(seen.pop())] != ch:
				return False
	if seen:
		return False
	return True

def main():
	print(valid_paranthesis('(]{}'))

if __name__ == '__main__':
	main()
