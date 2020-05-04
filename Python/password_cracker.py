"""
Author: Abhiram Ravi Bharadwaj
Source: HackerRank
Problem Link: https://www.hackerrank.com/challenges/password-cracker/problem
"""
def solve(passwords, string):
	if string == '':
		return ''
	if string in passwords:
		return passwords[string]
	passwords[string] = 'WRONG PASSWORD'
	for i in range(len(string) - 1, -1, -1):
		if string[:i] in passwords:
			future = solve(passwords, string[i:])
			if future != 'WRONG PASSWORD':
				passwords[string] = str(string[:i] + ' ' + future)
				break
	return passwords[string]

def check_possible(passwords, string):
	chars = set()
	for word in passwords:
		for ch in word:
			chars.add(ch)
	for ch in string:
		if ch not in chars:
			return False

def main():
	passwords = 'hello planet'
	string = 'helloworld'
	password_dict = {}
	if check_possible(passwords.split(), string) is False:
		print('WRONG PASSWORD')
		return
	for word in passwords.split():
		password_dict[word] = str(word)
	print(solve(password_dict, string))

if __name__ == '__main__':
	main()
