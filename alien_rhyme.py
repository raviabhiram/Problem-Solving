"""
Author: Abhiram Ravi Bharadwaj
Source: CodeJam
Problem: https://codingcompetitions.withgoogle.com/codejam/round/0000000000051635/0000000000104e05
"""
WORDS_USED = 0

def count(trie, is_root=False):
	global WORDS_USED
	words_used = 1 if ('end' in trie) else 0
	for key in trie:
		if key is not 'end':
			words_used += count(trie[key])
	if words_used >= 2 and not is_root:
		words_used -= 2
		WORDS_USED += 2
	return words_used

def insert(word, trie):
	if word[0] not in trie:
		trie[word[0]] = {}
	if len(word) == 1:
		trie[word[0]]['end'] = True
	else:
		insert(word[1:], trie[word[0]])
	return trie

def find_matchings(words):
	global WORDS_USED
	words = [word[::-1] for word in words]
	trie = {}
	for word in words:
		trie = insert(word, trie)
	count(trie, True)
	return

def main():
	global WORDS_USED
	for test in range(int(input())):
		WORDS_USED = 0
		words = []
		for word in range(int(input())):
			words.append(input())
		find_matchings(words)
		print('Case #', test + 1, ': ', WORDS_USED, sep='')

if __name__ == '__main__':
	main()
