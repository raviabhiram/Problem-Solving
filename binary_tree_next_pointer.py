"""
Author: Abhiram Ravi Bharadwaj
Source: Leetcode
Problem: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
"""
class Node:
	def __init__(self, val, left=None, right=None, next=None):
		self.val = val
		self.left = left
		self.right = right
		self.next = next

class Solution:
	def connect(self, root: 'Node') -> 'Node':
		if root is None:
			return None
		q = [root]
		while q:
			iterations = len(q)
			for i in range(iterations):
				current = q.pop(0)
				current.next = None if i == iterations - 1 else q[0]
				if current.left:
					q.append(current.left)
				if current.right:
					q.append(current.right)
		return root

def main():
	tree = Node(1, Node(2, Node(4), Node(5), Node(3, Node(6), Node(7))))
	Solution().connect(tree)

if __name__ == '__main__':
	main()
