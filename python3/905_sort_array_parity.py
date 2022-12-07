import unittest

class Solution:
	def sort_array_by_parity(self, nums: list[int]) -> list[int]:
		j = len(nums)
		for i in range(j):
			e = nums.pop(i)
			if e % 2 == 0:
				nums = [e] + nums
			else:
				nums.append(e)
				j -= 1
		return nums

class TestSolution(unittest.TestCase):
	def test_1(self):
		nums = [3,1,2,4]
		res = [2,4,3,1]
		self.assertCountEqual(Solution().sort_array_by_parity(nums), res)
	
	def test_2(self):
		nums = [0]
		res = [0]
		self.assertCountEqual(Solution().sort_array_by_parity(nums), res)
	
if __name__ == '__main__':
	unittest.main()	