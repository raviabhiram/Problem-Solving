"""
Author: Abhiram Ravi Bharadwaj
Source: Leetcode
Problem: https://leetcode.com/problems/group-anagrams/
"""

def group_anagrams(words):
	mapper = {}
	for word in words:
		lexical = ''.join(sorted(word))
		if lexical not in mapper:
			mapper[lexical] = []
		mapper[lexical].append(word)
	result = []
	for key in mapper:
		result.append(mapper[key])
	return result

def main():
	print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

if __name__ == '__main__':
	main()