import unittest

class Solution:
    
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1: return nums[0]
        if len(nums) >= 3:
            nums[2] += nums[0]
        for i in range(3, len(nums)):
            nums[i] = max(nums[i - 2] + nums[i], nums[i - 3] + nums[i])
        return max(nums[-2], nums[-1])

class TestSolution(unittest.TestCase):

    def test_1(self):
        nums: list[int] = [1,2,3,1]
        output: int = 4
        self.assertEqual(Solution().rob(nums), output)

    def test_2(self):
        nums: list[int] = [2,7,9,3,1]
        output: int = 12
        self.assertEqual(Solution().rob(nums), output)

if __name__ == "__main__":
    unittest.main()
