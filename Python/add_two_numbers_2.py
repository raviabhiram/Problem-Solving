"""
Author: Abhiram Ravi Bharadwaj
Source: Leetcode
Problem: https://leetcode.com/problems/add-two-numbers-ii/submissions/
"""
class ListNode:
	def __init__(self, x, next=None):
		self.val = x
		self.next = next

def addTwoNumbers(l1, l2):
	n1 = ''
	n2 = ''
	while l1:
		n1 += str(l1.val)
		l1 = l1.next
	while l2:
		n2 += str(l2.val)
		l2 = l2.next
	n3 = str(int(n1) + int(n2))
	return make_list(n3)

def make_list(num):
	if num:
		node = ListNode(num[0])
		node.next = make_list(num[1:])
		return node
	else:
		return None

def main():
	l1 = make_list('7243')
	l2 = make_list('564')
	rl = addTwoNumbers(l1, l2)
	while rl:
		print(rl.val, end='->')
		rl = rl.next

if __name__ == '__main__':
	main()
