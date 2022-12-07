import collections
import heapq
import unittest

class Solution:
	def network_delay_time(self, times: list[list[int]], n: int, k: int) -> int:
		weight = collections.defaultdict(dict)

		for u, v, w in times:
			weight[u][v] = w
		
		heap = [(0, k)]
		dist = {}

		while heap:
			time, u = heapq.heappop(heap)
			if u not in dist:
				dist[u] = time
				for v in weight[u]:
					heapq.heappush(heap, (dist[u] + weight[u][v], v))
		
		return max(dist.values()) if len(dist) == n else -1
		


class TestSolution(unittest.TestCase):
	def test_1(self):
		times = [[2,1,1],[2,3,1],[3,4,1]]
		n, k = 4, 2
		res = 2
		self.assertEqual(Solution().network_delay_time(times, n, k), res)
	
	def test_2(self):
		times = [[1,2,1]]
		n, k = 2, 1
		res = 1
		self.assertEqual(Solution().network_delay_time(times, n, k), res)
	
	def test_3(self):
		times = [[1,2,1]]
		n, k = 2, 2
		res = -1
		self.assertEqual(Solution().network_delay_time(times, n, k), res)

if __name__ == "__main__":
	unittest.main()