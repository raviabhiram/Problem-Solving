"""
Author: Abhiram Ravi Bharadwaj
Source: Leetcode
Problem: https://leetcode.com/problems/reverse-words-in-a-string/
"""
def reverse_string(s):
	s = s.split()
	for i in range(len(s) // 2):
		s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]
	return ' '.join(word for word in s)

def main():
	s = "the sky is blue"
	print(reverse_string(s))

if __name__ == '__main__':
	main()
