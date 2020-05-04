"""
Author: Abhiram Ravi Bharadwaj
Source: CodeChef
Problem: https://www.codechef.com/problems/DOMSOL
"""
def solve(values):
	result = [0] * len(values[0])
	result[0] = abs(values[0][0] - values[1][0])
	vertical = abs(values[0][0] - values[1][0]) + abs(values[0][1] - values[1][1])
	horizontal = abs(values[0][0] - values[0][1]) + abs(values[1][0] - values[1][1])
	result[1] = max(vertical, horizontal)
	for i in range(2, len(values[0])):
		vertical = abs((values[0][i] - values[1][i])) + result[i - 1]
		horizontal = abs(values[0][i] - values[0][i - 1]) + abs(values[1][i] - values[1][i - 1]) + result[i - 2]
		result[i] = max(vertical, horizontal)
	return result[-1]

def main():
	input()
	ip1 = input().split()
	ip2 = input().split()
	grid = [[int(x) for x in ip1]]
	grid.append([int(y) for y in ip2])
	print(solve(grid))

if __name__ == '__main__':
	main()
