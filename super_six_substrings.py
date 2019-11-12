"""
Author: Abhiram Ravi Bharadwaj
Source: Hackerrank
Problem: https://www.hackerrank.com/contests/hourrank-18/challenges/super-six-substrings/problem
"""
from collections import defaultdict
def count(s):
	reminder_map = defaultdict(int)
	ans = 0
	for ch in s:
		reminder_map[0] += 1
		current = int(ch)
		remainder = defaultdict(int)
		for key in reminder_map:
			remainder[(key * 10 + current) % 6] += reminder_map[key]
			if key == 0 and current == 0:
				remainder[0] -= 1
				ans += 1
		ans += remainder[0]
		reminder_map = remainder
	return ans

def main():
	print(count('06669939'))

if __name__ == '__main__':
	main()
