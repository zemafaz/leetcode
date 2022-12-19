import unittest

class Solution:

    def valid_path(self, n: int, edges: list[list[int]], source: int,
            destination: int, visited: set[int] = set()) -> bool:
        if destination >= n: return False
        if source == destination: return True
        if source in visited: return False
        found: bool = False
        for vertex1, vertex2 in edges:
            if source == vertex1:
                found = found or self.valid_path(n, edges, vertex2, destination, visited.union([source]))
            if source == vertex2:
                found = found or self.valid_path(n, edges, vertex1, destination, visited.union([source]))
            if found: break
        return found

class TestSolution(unittest.TestCase):

    def test_1(self):
        n: int = 3
        edges: list[list[int]] = [[0,1],[1,2],[2,0]]
        source: int = 0
        destination: int = 2
        output: bool = True
        self.assertEqual(Solution().valid_path(n, edges, source, destination),
                output)

    def test_2(self):
        n: int = 6
        edges: list[list[int]] = [[0,1],[0,2],[3,5],[5,4],[4,3]]
        source: int = 0
        destination: int = 5
        output: bool = False
        self.assertEqual(Solution().valid_path(n, edges, source, destination),
                output)

if __name__ == "__main__":
    unittest.main()
