import unittest

class Solution:
	def number_of_steps(self, num: int) -> int:
		n_steps = 0	

		while num > 0:
			n_steps += 1
			if num % 2 != 0:
				num -= 1
			else:
				num = num // 2

		return n_steps

	def number_of_steps_bin(self, num: int) -> int:
		steps = num == 0

		while num > 0:
			steps += 1 + (num & 1)
			num = num >> 1
		
		return steps - 1

class TestSolution(unittest.TestCase):
	def test_1(self):
		num = 14
		self.assertEqual(Solution().number_of_steps(num), 6)
	
	def test_2(self):
		num = 8
		self.assertEqual(Solution().number_of_steps(num), 4)
	
	def test_3(self):
		num = 123
		self.assertEqual(Solution().number_of_steps(num), 12)

	def test_1_bin(self):
		num = 123
		self.assertEqual(Solution().number_of_steps_bin(num), 12)

	

if __name__ == '__main__':
	unittest.main()