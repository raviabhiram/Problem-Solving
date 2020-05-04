# cook your dish here
"""
Author: Abhiram Ravi Bharadwaj
Source: CodeChef
Problem: https://www.codechef.com/problems/PALIN
"""
def find_next(number):
	if number == '9' * len(number):
		return '1' + ('0' * int(len(number) - 1)) + '1'
	num = [ch for ch in number]
	mid = int(len(num) // 2)
	if len(num) % 2 == 0:
		i, mid_i = mid - 1, mid - 1
		j, mid_j = i + 1, i + 1
	else:
		i, j, mid_i, mid_j = mid, mid, mid, mid
	while i >= 0 and num[i] == num[j]:
		i -= 1
		j += 1
	lesser = False
	if i < 0 or num[i] < num[j]:
		lesser = True
	if not lesser:
		while i >= 0:
			num[j] = num[i]
			i -= 1
			j += 1
	else:
		i = mid_i
		j = mid_j
		carry = False
		while num[i] == '9':
			num[i] = '0'
			num[j] = num[i]
			carry = True
			i -= 1
			j += 1
		if i >= 0 or carry:
			num[i] = str(int(num[i]) + 1)
		while i >= 0:
			num[j] = num[i]
			i -= 1
			j += 1
	return ''.join(num)

def main():
	for test in range(int(input())):
		print(find_next(input()))

if __name__ == '__main__':
	main()
