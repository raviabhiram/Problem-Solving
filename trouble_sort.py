"""
Author: Abhiram Ravi Bharadwaj
Source: CodeJam
Problem: https://codingcompetitions.withgoogle.com/codejam/round/00000000000000cb/00000000000079cb
"""

def catch_error(l):
	l1 = l[::2]
	l2 = l[1::2]
	l1 = sorted(l1)
	l2 = sorted(l2)
	res = []
	while l1 and l2:
		res.append(int(l1.pop(0)))
		res.append(int(l2.pop(0)))
	if l1:
		res.append(int(l1.pop(0)))
	if l2:
		res.append(int(l2.pop(0)))
	for i in range(len(res) - 1):
		if res[i] > res[i + 1]:
			print(i)
			return
	print('OK')

if __name__ == '__main__':
	for test in range((int(input()))):
		n = int(input())
		m = list(map(int, input().split(' ')))
		print('Case #', test + 1, ':', sep='', end=' ')
		catch_error(m)
