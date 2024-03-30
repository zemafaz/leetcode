import unittest
import math

class Solution:
	def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
		nums1_len = len(nums1)
		nums2_len = len(nums2)
		comb_len = nums1_len + nums2_len

		nums1_i = 0
		nums2_i = 0

		last_used = 2 if nums1_len == 0 else 1

		median = 0

		for i in range(comb_len):
			if nums1_i >= nums1_len:
				nums2_i += 1
				last_used = 2
			elif nums2_i >= nums2_len:
				nums1_i += 1
				last_used = 1
			if (nums1[nums1_i] <= nums2[nums2_i]):
				nums1_i += 1
				last_used = 1
			else:
				nums2_i += 1
				last_used = 2

			if (i == round(comb_len / 2) - 1):
				n1 = nums1[nums1_i - 1] if last_used == 1 else nums2[nums2_i - 1]

				if (comb_len % 2 == 1):
					median = n1
				else:
					n2 = None
					if nums1_i >= nums1_len:
						n2 = nums2[nums2_i]
					elif nums2_i >= nums2_len:
						n2 = nums1[nums1_i]
					else:
						n2 = nums1[nums1_i] if nums1[nums1_i] <= nums2[nums2_i] else nums2[nums2_i]
					median = (n1 + n2) / 2
				break

		return median


	def cheating(nums1: list[int], nums2: list[int]) -> float:
		nums = nums1+nums2
		nums.sort()
		ln=len(nums)

		if ln%2==1:
			return nums[(ln//2)]
		else:
			return (nums[(ln//2)]+nums[(ln//2)-1])/2



class TestSolution(unittest.TestCase):
	def test1(self):
		self.assertEqual(Solution.findMedianSortedArrays([1,3],[2]),2)

	def test2(self):
		self.assertEqual(Solution.findMedianSortedArrays([1,2],[3,4]),2.5)
	
	def test1_cheating(self):
		self.assertEqual(Solution.cheating([1,3],[2]),2)

	def test2_cheating(self):
		self.assertEqual(Solution.cheating([1,2],[3,4]),2.5)

if __name__ == '__main__':
	unittest.main()