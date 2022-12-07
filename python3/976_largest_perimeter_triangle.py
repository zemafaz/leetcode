import unittest

class Solution:
    
    def largest_perimeter_triangle(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            if nums[i] < nums[i+1] + nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]
        return 0

class TestSolution(unittest.TestCase):

    def test_1(self):
        nums = [2,1,2]
        output = 5
        self.assertEqual(Solution().largest_perimeter_triangle(nums), output)

    def test_2(self):
        nums = [1,2,1]
        output = 0
        self.assertEqual(Solution().largest_perimeter_triangle(nums), output)

if __name__ == "__main__":
    unittest.main()
