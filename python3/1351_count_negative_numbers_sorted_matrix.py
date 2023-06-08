import unittest

def count_negatives(grid: list[list[int]]) -> int:
    res = 0
    for _, row in enumerate(grid):
        low = 0
        high = len(row) - 1
        if row[high] >= 0:
            continue
        if row[low] < 0:
            res += len(row)
            continue
        while low < high - 1:
            middle = low + (high - low) // 2
            if row[middle] < 0:
                high = middle
            else:
                low = middle
        res += len(row) - high
    return res

class TestSolution(unittest.TestCase):

    def test_1(self):
        grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
        expected_output = 8
        result = count_negatives(grid)
        self.assertEqual(expected_output, result)

    def test_2(self):
        grid = [[3,2],[1,0]]
        expected_output = 0
        result = count_negatives(grid)
        self.assertEqual(expected_output, result)

if __name__ == '__main__':
    unittest.main()
