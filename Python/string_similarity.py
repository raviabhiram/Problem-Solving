"""
Author: Abhiram Ravi Bharadwaj
Source: HackerRank
Problem: https://www.hackerrank.com/challenges/string-similarity/problem
References: https://www.cs.cmu.edu/~ckingsf/bioinfo-lectures/zalg.pdf
					: https://www.hackerearth.com/practice/algorithms/string-algorithm/z-algorithm/tutorial/
"""

def main():
	s = 'ababaa'
	z = [0] * len(s)
	l = r = -1
	for i in range(1, len(s)):
		if i <= r:
			z[i] = min(r - i + 1, z[i - l])
		while i + z[i] < len(s) and s[z[i]] == s[i + z[i]]:
			z[i] += 1
		if i + z[i] - 1 > r:
			l = i
			r = i + z[i] - 1
	return sum(z) + len(s)

if __name__ == '__main__':
	main()
