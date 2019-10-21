"""
Author: Abhiram Ravi Bharadwaj
Source: HackerRank
Problem Link: https://www.hackerrank.com/challenges/beadornaments/problem
"""

def main(beads=[2, 2]):
	result = 1
	total_beads = 0
	for bead in beads:
		result *= bead ** (bead - 1)
		total_beads += bead
	result *= total_beads ** (len(beads) - 2)
	print(int(result) % 1000000007)

if __name__ == '__main__':
	beads = [4, 10]
	main(beads)
