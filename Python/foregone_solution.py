"""
Author: Abhiram Ravi Bharadwaj
Source: CodeJam
Problem: https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/0000000000088231
"""

def get_numbers(n):
	a = ''
	b = ''
	for i in range(len(n)):
		if n[i] == '4':
			a += '3'
			b += '1'
		else:
			a += n[i]
			if b != '':
				b += '0'
	return a, b

def main():
	T = int(input())
	for t in range(T):
		n = input()
		a, b = get_numbers(n)
		print('Case #', t + 1, ': ', sep='', end='')
		print(a, b)

if __name__ == '__main__':
	main()
