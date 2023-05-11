import unittest
import math

class Solution:

    def spiral_order(self, matrix: list[list[int]]) -> list[int]:
        n, m = len(matrix), len(matrix[0])
        pos_i, pos_j = 0, 0
        angle = 0
        res = []
        for _ in range(n*m):
            res.append(matrix[pos_i][pos_j])
            matrix[pos_i][pos_j] = 101
            next_pos_i, next_pos_j = pos_i + int(math.sin(angle)), pos_j + int(math.cos(angle))
            if (0 <= next_pos_i < n
                and 0 <= next_pos_j < m
                and matrix[next_pos_i][next_pos_j] != 101):
                pos_i, pos_j = next_pos_i, next_pos_j
            else:
                angle += math.pi/2
                pos_i, pos_j = pos_i + int(math.sin(angle)), pos_j + int(math.cos(angle)) 
        return res

class TestSolution(unittest.TestCase):

    def test_1(self):
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        res = [1,2,3,6,9,8,7,4,5]
        self.assertListEqual(Solution().spiral_order(matrix), res)

    def test_2(self):
        matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
        res = [1,2,3,4,8,12,11,10,9,5,6,7]
        self.assertListEqual(Solution().spiral_order(matrix), res)

if __name__ == '__main__':
    unittest.main()
