"""
Author: Abhiram Ravi Bharadwaj
Source: Leetcode
Problem: https://leetcode.com/problems/rotate-image/
"""
def rotate_image(matrix):
	m = len(matrix)
	for i in range(m // 2 + m % 2):
		for j in range(m // 2):
			matrix[i][j],matrix[m-1 - j][i] = matrix[m-1 - j][i],matrix[i][j]
			matrix[m-1 - j][i],matrix[m-1 - i][m-1 - j] = matrix[m-1 - i][m-1 - j],matrix[m-1 - j][i]
			matrix[m-1 - i][m-1 - j],matrix[j][m-1 - i] = matrix[j][m-1 - i],matrix[m-1 - i][m-1 - j]

def main():
	matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
	rotate_image(matrix)
	print(matrix)

if __name__ == '__main__':
	main()
