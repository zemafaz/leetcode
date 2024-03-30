import unittest

class Solution:
	def missing_number(self, nums: list[int])->int:
		n = len(nums)
		return n * (n+1) / 2 - sum(nums)

class TestSolution(unittest.TestCase):
	def test_1(self):
		nums = [3,0,1]
		self.assertEqual(Solution().missing_number(nums), 2)

	def test_2(self):
		nums = [0,1]
		self.assertEqual(Solution().missing_number(nums), 2)

	def test_3(self):
		nums = [9,6,4,2,3,5,7,0,1]
		self.assertEqual(Solution().missing_number(nums), 8)


if __name__ == "__main__":
	unittest.main()