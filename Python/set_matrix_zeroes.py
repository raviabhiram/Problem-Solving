"""
Author: Abhiram Ravi Bharadwaj
Source: Leetcode
Problem: https://leetcode.com/problems/set-matrix-zeroes/
"""

def set_zeroes(matrix):
	rows = set()
	columns = set()
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if matrix[i][j] == 0:
				rows.add(i)
				columns.add(j)
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if i in rows or j in columns:
				matrix[i][j] = 0

def main():
	m = [
		[1, 1, 1],
		[1, 0, 1],
		[1, 1, 1]
	]
	set_zeroes(m)
	print(m)

if __name__ == '__main__':
	main()
