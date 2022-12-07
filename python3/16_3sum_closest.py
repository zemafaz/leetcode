import unittest

class Solution:
	def three_sum_closest(self, nums: list[int], target: int) -> int:
		sol = []

		for i in range(len(nums)-2):
			for j in range(i+1, len(nums)-1):
				for k in range(j+1, len(nums)):
					poss = [nums[i], nums[j], nums[k]]
					dif_p = abs(self.sum_list(poss) - target)
					dif_s = abs(self.sum_list(sol) - target)
					if sol == [] or dif_p < dif_s:
						sol = poss
		return self.sum_list(sol)

	def sum_list(self, nums: list[int]) -> int:
		sum = 0
		for e in nums:
			sum += e
		return sum

	def three_sum_closest_sort(self, nums: list[int], target :int) -> int:
		nums.sort()
		result = nums[0] + nums[1] + nums[2]

		for i in range(len(nums) - 2):
			j, k = i+1, len(nums) - 1
			while j < k:
				sum = nums[i] + nums[j] + nums[k]
				if sum == target:
					return sum
				
				if abs(sum - target) < abs(result - target):
					result = sum
				
				if sum < target:
					j += 1
				elif sum > target:
					k -= 1
		return result

class TestSolution(unittest.TestCase):
	def test_1(self):
		self.assertEqual(Solution().three_sum_closest([-1,2,1,-4], 1), 2)
	
	def test_2(self):
		self.assertEqual(Solution().three_sum_closest([0,0,0], 1), 0)
	
	def test_1_sort(self):
		self.assertEqual(Solution().three_sum_closest_sort([-1,2,1,-4], 1), 2)
	
	def test_2_sort(self):
		self.assertEqual(Solution().three_sum_closest_sort([0,0,0], 1), 0)
if __name__ == '__main__':
	unittest.main()