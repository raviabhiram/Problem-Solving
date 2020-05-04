"""
Author: Abhiram Ravi Bharadwaj
Source: CodeChef
Problem: https://www.codechef.com/problems/VOGOZO
"""
def find_max(diff, types):
	max_dragons = 0
	current = types[0] - diff
	for type in types:
		if type - current >= diff:
			max_dragons += 1
			current = type
	return max_dragons

def main():
	ip = input().split()
	diff = int(ip[1])
	print(find_max(diff, sorted(list(map(int, input().split())))))

if __name__ == '__main__':
	main()
