"""
Author: Abhiram Ravi Bharadwaj
Source: Leetcode
Problem: https://leetcode.com/problems/generate-parentheses/submissions/
"""

def generateParenthesis(n):
	return solve(n, n, n, [], [])

def solve(n, left, right, current_sequence, answer):
	if len(current_sequence) == 2 * n:
		answer.append(''.join(current_sequence))
		return answer
	if left > 0:
		current_sequence.append('(')
		answer = solve(n, left - 1, right, current_sequence, answer)
		current_sequence.pop()
	if right > left:
		current_sequence.append(')')
		answer = solve(n, left, right - 1, current_sequence, answer)
		current_sequence.pop()
	return answer

def main():
	print(generateParenthesis(3))

if __name__ == '__main__':
	main()
