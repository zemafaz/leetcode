import unittest


def min_operations(nums: list[int]) -> int:
    nums.sort()
    nums_max = nums[0] + len(nums)
    res = 0
    for i, n in enumerate(nums):
        if n >= nums_max:
            res += len(nums) - i
            break
        if i + 1 != len(nums):
            if n == nums[i+1]:
                res += 1
        
    return res


class TestSolution(unittest.TestCase):

    def test_1(self):
        nums = [4,2,5,3]
        expected_output = 0
        self.assertEqual(min_operations(nums), expected_output)

    def test_2(self):
        nums = [1,2,3,5,6]
        expected_output = 1
        self.assertEqual(min_operations(nums), expected_output)

    def test_3(self):
        nums = [1,10,100,1000]
        expected_output = 3
        self.assertEqual(min_operations(nums), expected_output)

if __name__ == "__main__":
    unittest.main()
