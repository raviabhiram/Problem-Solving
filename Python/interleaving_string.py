"""
Author: Abhiram Ravi Bharadwaj
Source: Leetcode
Problem: https://leetcode.com/problems/interleaving-string/
"""
def interLeavingStrings(s1, s2, s3):
	l1, l2, l3 = len(s1), len(s2), len(s3)
	if l1 + l2 != l3:
		return False
	dp = [True for _ in range(l2 + 1)]
	for i in range(1, l2 + 1):
		dp[i] = dp[i - 1] and s2[i - 1] == s3[i - 1]
	for i in range(1, l1 + 1):
		dp[0] = (dp[0] and s1[0] == s3[0])
		for j in range(1, l2 + 1):
			dp[j] = (dp[j] and s1[i - 1] == s3[i + j - 1]) or (dp[j - 1] and s2[j - 1] == s3[i + j - 1])
	return dp[l2]

def main():
	s1 = "aabcc"
	s2 = "dbbca"
	s3 = "aadbbcbcac"
	print(interLeavingStrings(s1, s2, s3))

if __name__ == '__main__':
	main()