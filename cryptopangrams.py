"""
Author: Abhiram Ravi Bharadwaj
Source: CodeJam
Problem: https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/000000000008830b
"""
def gcd(a, b):
	if b == 0:
		return a
	return gcd(b, a % b)

def main():
	for test in range(int(input())):
		input()
		ip = [int(x) for x in input().split()]
		decoded = [0] * (len(ip) + 1)
		i = 0
		while ip[i] == ip[i + 1]:
			i += 1
		mark = i + 1
		decoded[mark] = gcd(ip[mark], ip[mark - 1])
		for i in range(mark - 1, -1, -1):
			decoded[i] = ip[i] // decoded[i + 1]
		for i in range(mark + 1, len(decoded)):
			decoded[i] = ip[i - 1] // decoded[i - 1]
		a = ord('A')
		dict = {}
		nums = sorted(set(decoded))
		for i in range(26):
			dict[nums[i]] = chr(a + i)
		for i in range(len(decoded)):
			decoded[i] = dict[decoded[i]]
		print('Case #', test + 1, ': ', ''.join(decoded), sep='')

if __name__ == '__main__':
	main()
