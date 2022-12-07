import unittest

class Solution:
	def furthest_building(self, heights: list[int], bricks: int, ladders: int) -> int:
		res = 0
		
		for i in range(len(heights) - 1):
			building_1 = heights[i]
			building_2 = heights[i+1]

			if building_1 >= building_2:
				res += 1
			else:
				if building_2 - building_1 <= bricks:
					bricks = bricks - (building_2 - building_1)
					res += 1
				elif ladders > 0:
					ladders -= 1
					res += 1
				else:
					break
		return res

class TestSolution(unittest.TestCase):
	def test_1(self):
		heights = [4,2,7,6,9,14,12]
		bricks = 5
		ladders = 1
		self.assertEqual(Solution().furthest_building(heights, bricks, ladders), 4)
	
	def test_2(self):
		heights = [4,12,2,7,3,18,20,3,19]
		bricks = 10
		ladders = 2
		self.assertEqual(Solution().furthest_building(heights, bricks, ladders), 7)

	def test_3(self):
		heights = [14,3,19,3]
		bricks = 17
		ladders = 0
		self.assertEqual(Solution().furthest_building(heights, bricks, ladders), 3)

if __name__ == '__main__':
	unittest.main()
	