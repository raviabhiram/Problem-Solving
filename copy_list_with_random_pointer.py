"""
Author: Abhiram Ravi Bharadwaj
Source: Leetcode
Problem: https://leetcode.com/problems/copy-list-with-random-pointer/
"""
class Node:
	def __init__(self, val, next=None, random=None):
		self.val = val
		self.next = next
		self.random = random

class Solution:
	def copyRandomList(self, head):
		if head is None:
			return None
		current = head
		while current is not None:
			current.next = Node(current.val, current.next, None)
			current = current.next.next
		current = head
		while current is not None:
			if current.random:
				current.next.random = current.random.next
			current = current.next.next
		current = head
		new_head = head.next
		new_current = new_head
		while current is not None:
			current.next = new_current.next
			current = current.next
			if current is not None:
				new_current.next = current.next
				new_current = new_current.next
		return new_head

def main():
	node1 = Node(-1)
	node2 = Node(8)
	node3 = Node(7)
	node4 = Node(3)
	node5 = Node(4)
	node1.next = node2
	node1.random = node5
	node2.next = node3
	node2.random = node4
	node3.next = node4
	node4.next = node5
	node5.random = node1
	new_list = Solution().copyRandomList(node1)

if __name__ == '__main__':
	main()
