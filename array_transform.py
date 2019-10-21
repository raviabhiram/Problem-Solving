"""
Author: Abhiram Ravi Bharadwaj
Source: CodeChef
Problem Link: https://www.codechef.com/problems/ARRAYTRM
"""

def check_test(n=3, k=2, a=[1, 2, 2]):
	for i in range(2):
		count = 0
		reminder = a[i] % (k + 1)
		for num in a:
			if num % (k + 1) == reminder:
				count += 1
		if count == n - 1 or count == n:
			print('YES')
			return
	print('NO')
	return

def main():
	t = int(input())
	for test in range(t):
		ip = input().split(' ')
		n = int(ip[0])
		k = int(ip[1])
		a = [int(i) for i in input().split()]
		check_test(n, k, a)

if __name__ == '__main__':
	main()
