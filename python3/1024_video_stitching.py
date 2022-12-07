import unittest

class Solution:
	def video_stitching(self, clips: list[list[int]], time: int) -> int:
		clips.sort()
		end, end2, res = -1, 0, 0

		for i, j in clips:
			if end2 >= time or i > end2:
				break
			elif end < i <= end2:
				res, end = res + 1, end2
			end2 = max(end2, j)
		return res if end2 >= time else -1

class TestSolution(unittest.TestCase):
	def test_1(self):
		self.assertEqual(Solution().video_stitching([[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], 10), 3)
	
	def test_2(self):
		self.assertEqual(Solution().video_stitching([[0,1],[1,2]], 5), -1)
	
	def test_3(self):
		self.assertEqual(Solution().video_stitching([[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], 9), 3)
	
if __name__ == '__main__':
	unittest.main()
	
