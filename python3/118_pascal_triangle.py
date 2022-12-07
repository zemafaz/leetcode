import unittest

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        pascal_triangle = []
        for i in range(numRows):
            pascal_triangle.append([1 for _ in range(i+1)])
            for j in range(len(pascal_triangle[-1])):
                if j != 0 and j != len(pascal_triangle) - 1:
                    pascal_triangle[i][j] = pascal_triangle[i-1][j-1] + pascal_triangle[i-1][j]
        return pascal_triangle

class TestSolution(unittest.TestCase):
    def test_1(self):
        numRows = 5
        self.assertEqual(Solution().generate(numRows),[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]])

    def test_2(self):
        numRows = 1
        self.assertEqual(Solution().generate(numRows),[[1]])

if __name__ == '__main__':
    unittest.main()   