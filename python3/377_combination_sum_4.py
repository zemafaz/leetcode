import unittest

class Solution():
    def combination_sum_4(self, nums: list[int], target: int) -> int:
        self.res = 0

        def aux(target):
            for num in nums:
                if target - num == 0:
                    self.res += 1
                    return
                if target - num > 0:
                    aux(target-num)
        aux(target)
        return self.res

    def combination_sum_4_ef(self, nums:list[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if num <= i:
                    dp[i] += dp[i-num]
        return dp[target]

class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [1,2,3]
        target = 4
        output = 7
        self.assertEqual(Solution().combination_sum_4(nums, target), output)

    def test_2(self):
        nums = [9]
        target = 3
        output = 0
        self.assertEqual(Solution().combination_sum_4(nums, target), output)

    def test_1_ef(self):
        nums = [1,2,3]
        target = 4
        output = 7
        self.assertEqual(Solution().combination_sum_4_ef(nums, target), output)

    def test_2_ef(self):
        nums = [9]
        target = 3
        output = 0
        self.assertEqual(Solution().combination_sum_4_ef(nums, target), output)

if __name__ == "__main__":
    unittest.main()
