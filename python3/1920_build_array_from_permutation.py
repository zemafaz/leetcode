import unittest

def build_array(nums: list[int]) -> list[int]:
    for i in range(len(nums)):
        nums[i] = (nums[nums[i]] % len(nums)) * len(nums) + nums[i]

    for i in range(len(nums)):
        nums[i] = nums[i] // len(nums)
    return nums

class TestSolution(unittest.TestCase):

    def test_1(self):
        nums = [0,2,1,5,3,4]
        expected_output = [0,1,2,4,5,3]
        res = build_array(nums)
        self.assertListEqual(res, expected_output)

    def test_2(self):
        nums = [5,0,1,2,3,4]
        expected_output = [4,5,0,1,2,3]
        res = build_array(nums)
        self.assertListEqual(res, expected_output)

if __name__ == '__main__':
    unittest.main()
