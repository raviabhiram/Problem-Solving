"""
Author: Abhiram Ravi Bharadwaj
Source: Leetcode
Problem: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
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
		if root.left:
			root.left.next = root.right
			self.connect(root.left)
		if root.right:
			if root.next:
				root.right.next = root.next.left
			self.connect(root.right)
		return root

def main():
	tree = Node(1, Node(2, Node(4), Node(5), Node(3, Node(6), Node(7))))
	Solution().connect(tree)

if __name__ == '__main__':
	main()
