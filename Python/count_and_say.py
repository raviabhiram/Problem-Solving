"""
Author: Abhiram Ravi Bharadwaj
Source: Leetcode
Problem: https://leetcode.com/problems/count-and-say/
"""

def countAndSay(n: int) -> str:
	if n == 1:
		return "1"
	if n == 2:
		return "11"
	ans = "11"
	for i in range(3, n + 1):
		ans += '$'
		size = len(ans)
		count = 1
		temp = ''
		for j in range(1, size):
			if ans[j] != ans[j - 1]:
				temp += str(count)
				temp += ans[j - 1]
				count = 1
			else:
				count += 1
		ans = temp
	return ans

def main():
	print(countAndSay(4))

if __name__ == '__main__':
	main()
