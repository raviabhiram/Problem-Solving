"""
Author: Abhiram Ravi Bharadwaj
Source: CodeJam
Problem: https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/00000000000881da
"""

def find_path(n,lydia_path):
	path=''
	for i in range(len(lydia_path)):
		if lydia_path[i]=='S':
			path+='E'
		else:
			path+='S'
	return path

def main():
	T = int(input())
	for t in range(T):
		n = input()
		lydia_path = input()
		path = find_path(n, lydia_path)
		print('Case #', t + 1, ': ', path, sep='')

if __name__ == '__main__':
	main()
