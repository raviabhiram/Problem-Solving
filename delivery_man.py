"""
Author: Abhiram Ravi Bharadwaj
Source: CodeChef
Problem Link: https://www.codechef.com/problems/TADELIVE
"""

def main():
	n, x, y = input().split(' ')
	n, x, y = int(n), int(x), int(y)
	a = input().split(' ')
	b = input().split(' ')
	# a = [1, 2, 3, 4, 5]
	# b = [5, 4, 3, 2, 1]
	# x = 3
	# y = 3
	# n = 5
	diff = []
	for i in range(n):
		diff.append({
			'a': int(a[i]),
			'b': int(b[i]),
			'diff': int(a[i]) - int(b[i])
		})
	sorted_diff = sorted(diff, key=lambda entry: entry['diff'], reverse=True)
	total_tip = 0
	for entry in sorted_diff:
		if entry['diff'] > 0:
			if x > 0:
				total_tip += entry['a']
				x -= 1
			else:
				total_tip += entry['b']
				y -= 1
		else:
			if y > 0:
				total_tip += entry['b']
				y -= 1
			else:
				total_tip += entry['a']
				x -= 1
	print(total_tip)
	return total_tip

if __name__ == '__main__':
	main()
