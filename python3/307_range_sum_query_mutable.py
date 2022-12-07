import unittest

class NumArray:
    def __init__(self, nums: list[int]):
        self.nums = nums

    def update(self, index: int, val: int) -> None:
        self.nums[index] = val

    def sum_range(self, left: int, right: int) -> int:
        return sum(self.nums[left:right+1])

class NumArrayPythonTrickery:
    def __init__(self, nums):
        self.update = nums.__setitem__
        self.sum_range = lambda i, j: sum(nums[i:j+1])

class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = NumArray([1,3,5])
        left = 0
        right = 2
        output = 9
        self.assertEqual(nums.sum_range(left, right), output)
        index = 1
        val = 2
        res = [1,2,5]
        nums.update(index, val)
        self.assertEqual(nums.nums, res)
        left = 0
        right = 2
        output = 8
        self.assertEqual(nums.sum_range(left, right), output)

if __name__ == '__main__':
    unittest.main()
