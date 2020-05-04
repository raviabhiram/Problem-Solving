"""
Author: Abhiram Ravi Bharadwaj
Source: CodeJam
Problem: https://codingcompetitions.withgoogle.com/codejam/round/00000000000516b9/0000000000134c90
"""
def make_move(dict, moves):
	if len(moves) >= 500:
		return None, 'IMPOSSIBLE'
	move = 0
	if len(dict['P']) > 0:
		move |= 4
	if len(dict['R']) > 0:
		move |= 2
	if len(dict['S']) > 0:
		move |= 1
	if move == 7:
		return None, 'IMPOSSIBLE'
	if move == 6:
		return dict['P'], moves + 'P'
	if move == 3:
		return dict['R'], moves + 'R'
	if move == 5:
		return dict['S'], moves + 'S'
	if move == 4:
		return None, moves + 'S'
	if move == 2:
		return None, moves + 'P'
	if move == 1:
		return None, moves + 'R'

def solve(a):
	moves = ''
	i = 0
	while a:
		dict = {'P': set(), 'R': set(), 'S': set()}
		for word in a:
			dict[word[i % len(word)]].add(word)
		a, moves = make_move(dict, moves)
		i += 1
	return moves

def main():
	for i in range(int(input())):
		strings = []
		max_iter = 0
		for j in range(int(input())):
			s = input()
			strings.append(s)
		print('Case #', i + 1, ': ', solve(strings), sep='')

if __name__ == '__main__':
	main()
