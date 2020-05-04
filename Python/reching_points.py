"""
Author: Abhiram Ravi Bharadwaj
Source: Leetcode
Problem: https://leetcode.com/problems/reaching-points/
"""
def reachingPoints(x1, y1, x2, y2):
	while x2 >= x1 and y2 >= y1 and x2 != y2:
		if x2 > y2:
			if y2 > y1:
				x2 %= y2
			else:
				return (x2 - x1) % y2 == 0
		else:
			if x2 > x1:
				y2 %= x2
			else:
				return (y2 - y1) % x2 == 0
	return x1 == x2 and y1 == y2

def main():
	print(reachingPoints(int(input()), int(input()), int(input()), int(input())))

if __name__ == '__main__':
	main()
