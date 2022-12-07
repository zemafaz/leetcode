import unittest

class Solution:

    def increasing_triplet(self, nums: list[int]) -> bool:
        res = [nums[0]]
        for num in nums:
            if len(res) == 1 and res[0] < num:
                res.append(num)
            elif len(res) == 2 and res[1] < num:
                return True
            elif len(res) == 2 and res[0] >= num:
                res = [num]
            elif len(res) == 2 and res[1] >= num:
                res[1] = num
            else:
                res = [num]
        return False

class TestSolution(unittest.TestCase):

    def test_1(self):
        nums = [1,2,3,4,5]
        output = True
        self.assertEqual(Solution().increasing_triplet(nums), output)

    def test_2(self):
        nums = [5,4,3,2,1]
        output = False
        self.assertEqual(Solution().increasing_triplet(nums), output)

    def test_3(self):
        nums = [2,1,5,0,4,6]
        output = True
        self.assertEqual(Solution().increasing_triplet(nums), output)

if __name__ == "__main__":
    unittest.main()

