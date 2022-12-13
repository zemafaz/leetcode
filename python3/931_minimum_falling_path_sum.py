import unittest

class Solution:

    def min_falling_path_sum(self, matrix: list[list[int]]) -> int:

        def aux(matrix: list[list[int]], i: int, j: int, sum: int) -> int:
            sum += matrix[i][j]
            if i + 1 >= len(matrix):
                return sum
            res: int = aux(matrix, i + 1, j, sum)
            if j - 1 >= 0:
                res = min(res, aux(matrix, i + 1, j - 1, sum))
            if j + 1 < len(matrix[0]):
                res = min(res, aux(matrix, i + 1, j + 1, sum))
            return res
        
        res: int|None = None
        for j in range(len(matrix[0])):
            res = min(res, aux(matrix, 0, j, 0)) if res != None else aux(matrix, 0, j, 0)
        return res if res != None else 0

    def min_falling_path_sum_dp(self, matrix: list[list[int]]) -> int:

        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] += min(matrix[i-1][max(0,j-1)], matrix[i-1][j], matrix[i-1][min(len(matrix[0])-1,j+1)])
        return min(matrix[-1])

class TestSolution(unittest.TestCase):

    def test_1(self):
        matrix: list[list[int]] = [[2,1,3],[6,5,4],[7,8,9]]
        output: int = 13
        self.assertEqual(Solution().min_falling_path_sum(matrix), output)

    def test_2(self):
        matrix: list[list[int]] = [[-19,57],[-40,-5]]
        output: int = -59
        self.assertEqual(Solution().min_falling_path_sum(matrix), output)

    def test_1_dp(self):
        matrix: list[list[int]] = [[2,1,3],[6,5,4],[7,8,9]]
        output: int = 13
        self.assertEqual(Solution().min_falling_path_sum_dp(matrix), output)

    def test_2_dp(self):
        matrix: list[list[int]] = [[-19,57],[-40,-5]]
        output: int = -59
        self.assertEqual(Solution().min_falling_path_sum_dp(matrix), output)

if __name__ == "__main__":
    unittest.main()
