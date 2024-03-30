from bisect import bisect_left
import unittest

class Solution:
	def max_envelopes(self, envelopes: list[list[int]]):
		envelopes.sort(key=lambda x: (x[0], -x[1]))
		dp = []
		for _, height in envelopes:
			left = bisect_left(dp, height)
			if left == len(dp): dp.append(height)
			else: dp[left] = height
		return len(dp)


class TestSolution(unittest.TestCase):
	def test_1(self):
		envelopes = [[5,4],[6,4],[6,7],[2,3]]
		self.assertEqual(Solution().max_envelopes(envelopes), 3)
	
	def test_2(self):
		envelopes = [[1,1],[1,1],[1,1]]
		self.assertEqual(Solution().max_envelopes(envelopes), 1)
	
if __name__ == "__main__":
	unittest.main()	