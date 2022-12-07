import unittest
from list_node import ListNode

class Solution:
	@staticmethod
	def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
		return Solution.add_two_numbers_rec(l1, l2, 0)
	
	@staticmethod
	def add_two_numbers_rec(l1: ListNode, l2: ListNode, c: int) -> ListNode:
		val = (l1.val + l2.val + c) % 10
		carryover = (l1.val + l2.val + c) // 10

		if (l1.next == None and l2.next == None):
			if (carryover == 0):
				return ListNode(val, None)
			else:
				return ListNode(val, Solution.add_two_numbers_rec(ListNode(0), ListNode(0), carryover))
		else:
			l1_new = l1.next
			l2_new = l2.next

			if l1_new == None:
				l1_new = ListNode(0)
			if l2_new == None:
				l2_new = ListNode(0)
			return ListNode(val, Solution.add_two_numbers_rec(l1_new, l2_new, carryover))
	
	def other_sol(l1: ListNode, l2: ListNode):
		result = ListNode(0)
		result_tail = result
		carry = 0

		while l1 or l2 or carry:
			val1 = (l1.val if l1 else 0)
			val2 = (l2.val if l2 else 0)
			carry, out = divmod(val1 + val2 + carry, 10)

			result_tail.next = ListNode(out)
			result_tail = result_tail.next

			l1 = (l1.next if l1 else None)
			l2 = (l2.next if l2 else None)

		return result.next

class TestSolution(unittest.TestCase):
	def test1(self):
		num1 = ListNode.list_to_list_node([2,4,3])
		num2 = ListNode.list_to_list_node([5,6,4])
		numT = ListNode.list_to_list_node([7,0,8])
		# self.assertEqual(Solution.add_two_numbers(num1, num2), numT)
		self.assertEqual(Solution.other_sol(num1, num2), numT)
	
	def test2(self):
		num1 = ListNode.list_to_list_node([0])
		num2 = ListNode.list_to_list_node([0])
		numT = ListNode.list_to_list_node([0])
		# self.assertEqual(Solution.add_two_numbers(num1, num2), numT)
		self.assertEqual(Solution.other_sol(num1, num2), numT)

	
	def test3(self):
		num1 = ListNode.list_to_list_node([9,9,9,9,9,9,9])
		num2 = ListNode.list_to_list_node([9,9,9,9])
		numT = ListNode.list_to_list_node([8,9,9,9,0,0,0,1])
		# self.assertEqual(Solution.add_two_numbers(num1, num2), numT)
		self.assertEqual(Solution.other_sol(num1, num2), numT)


if __name__ == "__main__":
	unittest.main()