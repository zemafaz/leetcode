import unittest

class Solution:
    def num_rolls_to_target(self, n: int, k: int, target: int) -> int:
        memo = {}
        def dp(rem, target):
            if rem == 0:
                return 0 if target > 0 else 1
            if (rem, target) in memo:
                return memo[(rem, target)]
            res = 0
            for i in range(max(0,target-k), target):
                res += dp(rem-1, i)
            memo[(rem, target)] = res
            return res
        return dp(n, target) % (10 ** 9 + 7)

class TestSolution(unittest.TestCase):
    def test_1(self):
        n = 1
        k = 6
        target = 3
        output = 1
        self.assertEqual(Solution().num_rolls_to_target(n, k, target), output)
        
    def test_2(self):
        n = 2
        k = 6
        target = 7
        output = 6
        self.assertEqual(Solution().num_rolls_to_target(n, k, target), output)
        
    def test_3(self):
        n = 30
        k = 30
        target = 500
        output = 222616187
        self.assertEqual(Solution().num_rolls_to_target(n, k, target), output)
        
if __name__ == "__main__":
    unittest.main()
