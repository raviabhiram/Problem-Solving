"""
Author: Abhiram Ravi Bharadwaj
Source: HackerRank
Problem Link: https://www.hackerrank.com/challenges/matrix-rotation-algo/problem
"""
def rot_matrix(matrix, rot):
	og_rows = len(matrix) - 1
	og_cols = len(matrix[0]) - 1
	rows = 0
	cols = 0
	while rows <= (og_rows) / 2 and cols <= (og_cols) / 2:
		nums = []
		
		# Store all elements in the layer as a list.
		for i in range(cols, og_cols - cols + 1):
			nums.append(matrix[rows][i])
		for i in range(rows + 1, og_rows - rows + 1):
			nums.append(matrix[i][og_cols - cols])
		for i in range(og_cols - cols - 1, cols - 1, -1):
			nums.append(matrix[og_rows - rows][i])
		for i in range(og_rows - rows - 1, rows, -1):
			nums.append(matrix[i][cols])
		cur_rot = rot % len(nums)  # Compute the rotation factor for this layer.
		nums = nums[cur_rot:] + nums[:cur_rot]  # Rotate the elements of this layer.

		# Update the elements of this layer back into the matrix.
		for i in range(cols, og_cols - cols + 1):
			matrix[rows][i] = nums.pop(0)
		for i in range(rows + 1, og_rows - rows + 1):
			matrix[i][og_cols - cols] = nums.pop(0)
		for i in range(og_cols - cols - 1, cols - 1, -1):
			matrix[og_rows - rows][i] = nums.pop(0)
		for i in range(og_rows - rows - 1, rows, -1):
			matrix[i][cols] = nums.pop(0)
		rows += 1
		cols += 1
	for row in matrix:
		print(' '.join(row))

def main():
	# rows = 4
	# columns = 4
	# rot = 7
	rows, columns, rot = map(int, input().strip().split())
	# matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
	# matrix = [[1, 2, 3, 4], [7, 8, 9, 10], [13, 14, 15, 16], [19, 20, 21, 22], [25, 26, 27, 28]]
	matrix = []
	for i in range(rows):
		matrix.append(list(input().strip().split()))
	rot_matrix(matrix, rot)

if __name__ == '__main__':
	main()
