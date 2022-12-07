import unittest
from collections import deque

class Solution:
    def contains_nearby_duplicate(self, nums: list[int], k: int) -> bool:
        current = deque(maxlen=k)
        for num in nums:
            if num in current:
                return True
            current.append(num)
        return False

class TestSolution(unittest.TestCase):
    
    def test_1(self):
        nums = [1,2,3,1]
        k = 3
        output = True
        self.assertEqual(Solution().contains_nearby_duplicate(nums, k), output)
    
    def test_2(self):
        nums = [1,0,1,1]
        k = 1
        output = True
        self.assertEqual(Solution().contains_nearby_duplicate(nums, k), output)
    
    def test_3(self):
        nums = [1,2,3,1,2,3]
        k = 2
        output = False
        self.assertEqual(Solution().contains_nearby_duplicate(nums, k), output)

if __name__ == "__main__":
    unittest.main()
