import unittest

class Solution:

    def maximum_score_base(self, nums: list[int], k: int) -> int:
        i = k
        j = k
        res = nums[k]
        while True:
            res = max(res, min(nums[i:j+1]) * (j - i + 1))
            if i == 0 and j == len(nums) - 1:
                break
            if i == 0:
                j += 1
                continue
            if j == len(nums) - 1:
                i -= 1
                continue
            if nums[i-1] > nums[j+1]:
                i -= 1
            else:
                j += 1

        return res

class TestSolution(unittest.TestCase):

    def test_1(self):
        nums = [1,4,3,7,4,5]
        k = 3
        output = 15
        self.assertEqual(Solution().maximum_score_base(nums, k), output)

    def test_2(self):
        nums = [5,5,4,5,4,1,1,1]
        k = 0
        output = 20
        self.assertEqual(Solution().maximum_score_base(nums, k), output)

if __name__ == "__main__":
    unittest.main()
