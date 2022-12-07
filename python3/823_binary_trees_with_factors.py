import unittest

class Solution:
    def num_factory_binary_trees(self, arr: list[int]) -> int:
        arr.sort()
        dp = [1 for _ in range(len(arr))]
        for j in range(len(arr)):
            bt = [arr[j]]
            i = 0
            while i < len(bt):
                for n2 in arr:
                    if bt[i] % n2 == 0 and bt[i] // n2 in arr:
                        dp[j] += dp[arr.index(n2)] + dp[arr.index(bt[i]//n2)] - 1
                        # bt.append(bt[i] // n2)
                        # bt.append(n2)
                        # dp[j] += 1
                i += 1
        return sum(dp)

class TestSolution(unittest.TestCase):
    def test_1(self):
        arr = [2,4]
        output = 3
        self.assertEqual(Solution().num_factory_binary_trees(arr), output)

    def test_2(self):
        arr = [2,4,5,10]
        output = 7
        self.assertEqual(Solution().num_factory_binary_trees(arr), output)

if __name__ == "__main__":
    unittest.main()
