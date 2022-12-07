import unittest

class Solution:
    def longest_consecutive(self, nums: list[int]) -> int:

        longest_streak = 0
        nums_set = set(nums)
        
        for num in nums_set:
            if num - 1 not in nums_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in nums_set:
                    current_num += 1
                    current_streak += 1
                
                longest_streak = max(longest_streak, current_streak)

        return longest_streak

class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [100, 4, 200, 1, 3, 2]
        self.assertEqual(Solution().longest_consecutive(nums), 4)

    def test_2(self):
        nums = [0,3,7,2,5,8,4,6,0,1]
        self.assertEqual(Solution().longest_consecutive(nums), 9)


if __name__ == '__main__':
    unittest.main()
