import unittest

class Solution:
    def search_range(self, nums: list[int], target: int) -> list[int]:
        if not nums: return [-1,-1]
        
        lower = 0
        upper = len(nums) - 1
        res = [-1, -1]

        while lower != upper and lower != upper - 1:
            middle = upper - (upper-lower) // 2
            if target == nums[middle]:
                res = [middle, middle]
                break
            elif target > nums[middle]:
                lower = middle + 1
            else:
                upper = middle - 1

        if res == [-1, -1]: return res

        while lower != res[0] - 1:
            middle = lower + (res[0] - lower) // 2
            if nums[middle] == target:
                res[0] = middle
            else:
                lower = middle
        
        while upper != res[1] + 1:
            middle = upper - (upper - res[1]) // 2
            if nums[middle] == target:
                res[1] = middle
            else:
                upper = middle
        return res

class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [5,7,7,8,8,10]
        target = 8
        output = [3,4]
        self.assertEqual(Solution().search_range(nums, target), output)
    
    def test_2(self):
        nums = [5,7,7,8,8,10]
        target = 6
        output = [-1,-1]
        self.assertEqual(Solution().search_range(nums, target), output)
    
    def test_3(self):
        nums = []
        target = 0
        output = [-1,-1]
        self.assertEqual(Solution().search_range(nums, target), output)
    
if __name__ == '__main__':
    unittest.main()