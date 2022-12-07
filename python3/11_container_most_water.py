import unittest

class Solution:
	def max_area(self, height: list[int]) -> int:
		max_area = 0
		x1 = 0
		x2 = len(height) - 1

		while x1 < x2:
			x = x2 - x1
			y = min(height[x1], height[x2])
			area = x * y

			if area > max_area:
				max_area = area

			if (height[x1] > height[x2]):
				x2 =- 1
			else:
				x1 += 1
			
			if (x2 - x1 <= y):
				break

		return max_area

class TestSolution(unittest.TestCase):
	def test_1(self):
		self.assertEqual(Solution().max_area([1,8,6,2,5,4,8,3,7]), 49)
	
	def test_2(self):
		self.assertEqual(Solution().max_area([1,1]), 1)
	

if __name__ == '__main__':
	unittest.main()