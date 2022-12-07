import unittest
import collections

class Solution:
	def critical_connections(self, n: int, connections: list[list[int]]) -> list[list[int]]:
		def dfs(rank, curr, prev):
			low[curr], result = rank, []
			for neighbor in edges[curr]:
				if neighbor == prev: continue
				if not low[neighbor]:
					result += dfs(rank + 1, neighbor, curr)
				low[curr] = min(low[curr], low[neighbor])
				if low[neighbor] >= rank + 1:
					result.append([curr, neighbor])
			return result
		
		low, edges = [0] * n, collections.defaultdict(list)
		for u, v in connections:
			edges[u].append(v)
			edges[v].append(u)
		
		return dfs(1, 0, -1)

class TestSolution(unittest.TestCase):
	def test_1(self):
		n = 4
		connections = [[0,1],[1,2],[2,0],[1,3]]
		self.assertEqual(Solution().critical_connections(n, connections), [[1,3]])
	
	def test_2(self):
		n = 2
		connections = [[0,1]]
		self.assertEqual(Solution().critical_connections(n, connections), [[0,1]])
	
if __name__ == '__main__':
	unittest.main()