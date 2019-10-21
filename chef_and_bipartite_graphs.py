"""
Author: Abhiram Ravi Bharadwaj
Source: CodeChef
Problem Link: https://www.codechef.com/problems/ICPC16F
"""

def main():
	t = int(input())
	for test in range(t):
		ip = input().split()
		n, m, d, D = int(ip[0]), int(ip[1]), int(ip[2]), int(ip[3])
		D = min(D, n)
		if (m < d * n) or (m > D * n):
			print(-1)
			continue
		e = m // n
		for i in range(n):
			for j in range(e):
				print(str(i+1), str((i + j) % n + 1))
		f = m % n
		for i in range(f):
			print(str(i+1), str((i + e) % n + 1))

if __name__ == '__main__':
	main()
