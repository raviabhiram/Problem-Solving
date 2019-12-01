"""
Author: Abhiram Ravi Bharadwaj
Source: CodeChef
Problem: https://www.codechef.com/problems/CULPRO
"""
def find_max_people(enter, exit):
	times = sorted(enter + exit)
	enter = set(enter)
	people, max_people = 0, 0
	for time in times:
		people = people + 1 if time in enter else people - 1
		max_people = max(max_people, people)
	return max_people

def main():
	events = int(input())
	enter, exit = [], []
	for i in range(events):
		ip = input().split()
		enter.append(int(ip[0]))
		exit.append(int(ip[1]))
	print(find_max_people(enter, exit))

if __name__ == '__main__':
	main()
