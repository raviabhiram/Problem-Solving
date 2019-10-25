"""
Author: Abhiram Ravi Bharadwaj
Source: CodeChef
Problem: https://www.codechef.com/problems/COINS
"""
MAX_VALUES = {}
def find_max(n):
	if n <= 0:
		return 0
	if n in MAX_VALUES:
		return MAX_VALUES[n]
	MAX_VALUES[n] = max(n, find_max(n // 2) + find_max(n // 3) + find_max(n // 4))
	return MAX_VALUES[n]

def main():
	while True:
		try:
			n = int(input())
			print(find_max(n))
		except:
			break

if __name__ == '__main__':
	main()
