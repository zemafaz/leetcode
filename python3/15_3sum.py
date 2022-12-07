import unittest

class Solution:
	def three_sum(self, nums: list[int]) -> list[list[int]]:
		res = []
		if len(nums) <= 3:
			return res

		for i in range(0, len(nums) - 2):
			for j in range(i+1, len(nums) - 1):
				repeated = False
				for e in res:
					if nums[i] in e and nums[j] in e:
						repeated = True
						break
				if repeated == True:
					continue
				for k in range(j+1, len(nums)):
					if nums[i] + nums[j] + nums[k] == 0:
						res.append([nums[i], nums[j], nums[k]])

		return res

class TestSolution(unittest.TestCase):
	def test_1(self):
		self.assertEqual(Solution().three_sum([-1,0,1,2,-1,-4]), [[-1, 0, 1],[-1, 2, -1]])
	
	def test_2(self):
		self.assertEqual(Solution().three_sum([]), [])
	
	def test_3(self):
		self.assertEqual(Solution().three_sum([0]), [])
		
if __name__ == '__main__':
	unittest.main()