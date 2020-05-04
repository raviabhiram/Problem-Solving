"""
Author: Abhiram Ravi Bharadwaj
Source: HackerRank
Problem Link: https://www.hackerrank.com/challenges/bigger-is-greater/problem
"""

def bigger_is_greater(word):
	length = len(word) - 1
	max = length
	for j in range(max - 1, -1, -1):  # Loop to find the first letter from the right that can be replaced.
		if word[j] > word[max]:
			max = j
		if word[j] < word[max]:
			for i in range(length, j, -1):  # Find the smallest letter on the right to replace with.
				if word[i] > word[j]:
					new_word = word[:j] + word[i]
					word = word[j + 1:i] + word[j] + word[i + 1:]
					new_word += word[len(word)::-1]
					return new_word
	return 'no answer'

def main():
	word = 'dkhc'
	result = bigger_is_greater(word)
	print(result)

if __name__ == '__main__':
	main()
