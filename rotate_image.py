"""
Author: Abhiram Ravi Bharadwaj
Source: Leetcode
Problem: https://leetcode.com/problems/rotate-image/
"""
def rotate_image(matrix):
	m = len(matrix)
	n = m - 1
	for i in range(m // 2 + m % 2):
		for j in range(m // 2):
			temp = matrix[i][j]
			matrix[i][j] = matrix[n - j][i]
			matrix[n - j][i] = matrix[n - i][n - j]
			matrix[n - i][n - j] = matrix[j][n - i]
			matrix[j][n - i] = temp

def main():
	matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
	rotate_image(matrix)
	print(matrix)

if __name__ == '__main__':
	main()
