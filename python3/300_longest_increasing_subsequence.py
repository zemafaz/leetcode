import unittest
import bisect

class Solution:
    def length_of_LIS_dp(self, nums: list[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        return max(dp)

    def length_of_LIS_bs(self, nums: list[int]) -> int:
        sub = []
        for n in nums:
            if len(sub) == 0 or sub[-1] < n:
                sub.append(n)
            else:
                index = bisect.bisect_left(sub, n)
                sub[index] = n
        return len(sub)

class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [10,9,2,5,3,7,101,18]
        output = 4
        self.assertEqual(Solution().length_of_LIS_dp(nums), output)

    def test_2(self):
        nums = [0,1,0,3,2,3]
        output = 4
        self.assertEqual(Solution().length_of_LIS_dp(nums), output)

    def test_3(self):
        nums = [0,1,0,3,2,3]
        output = 4
        self.assertEqual(Solution().length_of_LIS_dp(nums), output)

    def test_1_bs(self):
        nums = [10,9,2,5,3,7,101,18]
        output = 4
        self.assertEqual(Solution().length_of_LIS_dp(nums), output)

    def test_2_bs(self):
        nums = [0,1,0,3,2,3]
        output = 4
        self.assertEqual(Solution().length_of_LIS_dp(nums), output)

    def test_3_bs(self):
        nums = [0,1,0,3,2,3]
        output = 4
        self.assertEqual(Solution().length_of_LIS_dp(nums), output)

if __name__ == '__main__':
    unittest.main()
