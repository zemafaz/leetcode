import unittest

class Solution:
    def num_times_all_blue(self, flips: list[int]) -> int:
        right = -1
        res = 0

        for i in range(len(flips)):
            right = max(right, flips[i])
            if right == i + 1:
                res += 1
        
        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        flips = [3,2,4,1,5]
        self.assertEqual(Solution().num_times_all_blue(flips), 2)

    def test_2(self):
        flips = [4,1,2,3]
        self.assertEqual(Solution().num_times_all_blue(flips), 1)
    
if __name__ == '__main__':
    unittest.main()