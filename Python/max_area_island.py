"""
Author: Abhiram Ravi Bharadwaj
Source: Leetcode
Problem: https://leetcode.com/problems/max-area-of-island/
"""
def maxAreaOfIsland(grid):
	maxArea = 0
	visited = set()
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == 1 and (i, j):
				count = getIslandArea(grid, i, j, visited, 0, len(grid), len(grid[0]))
				maxArea = count if count > maxArea else maxArea
	return maxArea

def getIslandArea(grid, i, j, visited, area, m, n):
	if (i, j) in visited:
		return area

	visited.add((i, j))
	area += 1

	# Check left
	if j > 0 and grid[i][j - 1] == 1:
		area = getIslandArea(grid, i, j - 1, visited, area, m, n)

	# Check right
	if j < n - 1 and grid[i][j + 1] == 1:
		area = getIslandArea(grid, i, j + 1, visited, area, m, n)

	# Check up
	if i > 0 and grid[i - 1][j] == 1:
		area = getIslandArea(grid, i - 1, j, visited, area, m, n)

	# Check down
	if i < m - 1 and grid[i + 1][j] == 1:
		area = getIslandArea(grid, i + 1, j, visited, area, m, n)

	return area

def main():
	print(maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
	                       [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
	                       [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
	                       [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))

if __name__ == '__main__':
	main()
