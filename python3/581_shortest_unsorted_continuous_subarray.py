import unittest

class Solution:
	def find_unsorted_subarray(self, nums: list[int]) -> int:
		n = len(nums)

		if n > 1:
			for i in range(1, len(nums)):
				if nums[i] >= nums[i-1]:
					n -= 1
					if n == 0:
						return n
				else:
					break
			
			for i in range(len(nums) - 1, 1, -1):
				if nums[i] >= nums[i-1]:
					n -= 1
					if n == 0:
						return n
				else:
					break
		else:
			n = 0
		
		return n

class TestSolution(unittest.TestCase):
	def test_1(self):
		nums = [2,6,4,8,10,9,15]
		self.assertEqual(Solution().find_unsorted_subarray(nums), 5)
	
	def test_2(self):
		nums = [1,2,3,4]
		self.assertEqual(Solution().find_unsorted_subarray(nums), 0)
	
	def test_3(self):
		nums = [1]
		self.assertEqual(Solution().find_unsorted_subarray(nums), 0)
	
if __name__ == '__main__':
	unittest.main()