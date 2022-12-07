import unittest


class Solution:
    def kth_smallest(self, matrix: list[list[int]], k: int) -> int:
        pos = set()
        pos.add((0, 0, matrix[0][0]))
        while k > 1:
            min_pos = min(pos,key=lambda x: x[2])
            if min_pos[0] + 1 < len(matrix):
                i, j = min_pos[0] + 1, min_pos[1]
                pos.add((i, j,matrix[i][j]))
            if min_pos[1] + 1 < len(matrix[0]):
                i, j = min_pos[0], min_pos[1] + 1
                pos.add((i,j,matrix[i][j]))
            pos.remove(min_pos)
            k -= 1
        return min(pos,key=lambda x: x[2])[2]

class TestSolution(unittest.TestCase):
    def test_1(self):
        matrix = [[1,5,9],[10,11,13],[12,13,15]]
        k = 8
        output = 13
        self.assertEqual(Solution().kth_smallest(matrix, k), output)
    
    def test_2(self):
        matrix = [[-5]]
        k = 1
        output = -5
        self.assertEqual(Solution().kth_smallest(matrix, k), output)
    
if __name__ == "__main__":
    unittest.main()