"""
Author: Abhiram Ravi Bharadwaj
Source: CodeChef
Problem: https://www.codechef.com/problems/ORDERS
"""
def find_og_pos(n, moves):
	og_pos = [(i + 1) for i in range(n)]
	for i in range(n - 1, -1, -1):
		if moves[i] != 0:
			replaces = i - moves[i]
			replace_rank = og_pos[replaces]
			og_pos.pop(replaces)
			og_pos.insert(i, replace_rank)
	return og_pos

def main():
	for test in range(int(input())):
		n = int(input())
		ip = input().split()
		print(' '.join(str(x) for x in find_og_pos(n, [int(x) for x in ip])))

if __name__ == '__main__':
	main()
