from typing import List
import unittest

class Solution:

	@staticmethod
	def two_sum(nums: list[int], target: int) -> List[int]:
		for i in range(len(nums)):
			for j in range(i+1,len(nums)):
				if nums[i] + nums[j] == target:
					return [i, j]

	def optimal(nums: list[int], target: int) -> List[int]:
		hashmap = {}
		for i in range(len(nums)):
			complement = target - nums[i]
			if complement in hashmap:
				return [hashmap[complement], i]
			else:
				hashmap[nums[i]] = i


class TestSolution(unittest.TestCase):

	def test1(self):
		#self.assertEqual(Solution.two_sum([2,7,11,15], 9), [0,1])
		self.assertEqual(Solution.optimal([2,7,11,15], 9), [0,1])
	
	def test2(self):
		#self.assertEqual(Solution.two_sum([3,2,4], 6), [1,2])
		self.assertEqual(Solution.optimal([3,2,4], 6), [1,2])


	def test3(self):
		#self.assertEqual(Solution.two_sum([3,3], 6), [0,1])
		self.assertEqual(Solution.optimal([3,3], 6), [0,1])


if __name__ == "__main__":
	unittest.main()