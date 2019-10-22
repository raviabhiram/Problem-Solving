"""
Author: Abhiram Ravi Bharadwaj
Source: Leetcode
Problem: https://leetcode.com/problems/longest-palindromic-substring/
"""

def expand_around_i(s, i, start):
	j = i - start
	k = i + start
	while j >= 0 and k < len(s) and s[j] == s[k]:
		j -= 1
		k += 1
	return i - (j + 1)

def lps_manacher(s):
	s = '#' + '#'.join(s) + '#'
	p = [0] * len(s)
	l, r, c = 0, 0, 0

	for i in range(1, len(s)):
		mirror = 2 * c - i
		p[i] = min(p[mirror], r - i) if mirror >= 0 and i <= r else 0
		p[i] = max(expand_around_i(s, i, p[i]), p[i])
		if p[i] > p[c]:
			l, r, c = i - p[i], i + p[i], i
	return s[l:r + 1].replace('#', '')

def main():
	print(lps_manacher('abb'))

if __name__ == '__main__':
	main()
