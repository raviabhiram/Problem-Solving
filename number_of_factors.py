"""
Author: Abhiram Ravi Bharadwaj
Source: CodeChef
Problem: https://www.codechef.com/problems/NUMFACT
"""
def get_factor(number):
	for i in range(2, int(number ** 0.5) + 1):
		if number % i == 0:
			return i
	return None

def find_factors(numbers, dict):
	number = numbers.pop(0)
	keys = dict.keys()
	factor = get_factor(number)
	if factor is None:
		if number not in keys:
			dict[number] = 0
		dict[number] += 1
	else:
		numbers.append(factor)
		numbers.append(number / factor)
	return numbers, dict

def main():
	T = int(input())
	for test in range(T):
		N = int(input())
		numbers = input()
		numbers = [int(x) for x in numbers.split()]
		value = 1
		dict = {}
		while len(numbers) > 0:
			numbers, dict = find_factors(numbers, dict)
		for key in dict.keys():
			value *= (dict[key] + 1)
		print(value)

if __name__ == '__main__':
	main()
