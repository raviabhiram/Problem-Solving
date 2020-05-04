"""
Author: Abhiram Ravi Bharadwaj
Source: Leetcode
Problem: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
"""
class TreeNode:
	def __init__(self, x, left=None, right=None):
		self.val = x
		self.left = left
		self.right = right

class Solution:
	def zigzagLevelOrder(self, root):
		if root is None:
			return []
		main_list = []
		turn = True
		q = [root]
		while q:
			temp = []
			for i in range(len(q)):
				node = q.pop(0)
				temp.append(node.val)
				if node.left:
					q.append(node.left)
				if node.right:
					q.append(node.right)
			if turn:
				main_list.append(temp)
			else:
				main_list.append(temp[::-1])
			turn = not turn
		return main_list

def main():
	tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
	print(Solution().zigzagLevelOrder(tree))

if __name__ == '__main__':
	main()
