import unittest

class Solution:

    def diagonal_sum(self, mat: list[list[int]]) -> int:
        n = len(mat)
        sum = 0
        j = n - 1
        for i in range(n):
            if i == j:
                sum += mat[i][j]
            else:
                sum += mat[i][i] + mat[i][j]
            j -= 1
        return sum
                    

class TestSolution(unittest.TestCase):

    def test_1(self):
        mat = [[1,2,3],
               [4,5,6],
               [7,8,9]]
        res: int = 25
        self.assertEqual(Solution().diagonal_sum(mat), res)

    def test_2(self):
        mat = [[1,1,1,1],
               [1,1,1,1],
               [1,1,1,1],
               [1,1,1,1]]
        res: int = 8
        self.assertEqual(Solution().diagonal_sum(mat), res)

    def test_3(self):
        mat = [[5]]
        res: int = 5
        self.assertEqual(Solution().diagonal_sum(mat), res)

if __name__ == '__main__':
    unittest.main()
